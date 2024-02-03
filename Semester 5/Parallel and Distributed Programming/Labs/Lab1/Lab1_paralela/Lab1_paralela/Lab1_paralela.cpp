#include <iostream>
#include <list>
#include <unordered_map>
#include <fstream>
#include <ctime>
#include <vector>
#include <random>
#include <mutex>
#include <thread>
#include <chrono>

#define CREATOR_THREAD_COUNT 4
#define TRANSACTIONS_PER_THREAD 500

typedef struct {
    int sourceAccountId;
    int destinationAccountId;
    int amount;
    int serialNumber;
} OPERATION;

typedef struct {
    int id;
    int balance;
    int initialBalance;
    std::list<OPERATION> log;
} ACCOUNT;

std::unordered_map<int, ACCOUNT> _accounts;
std::list<OPERATION> _operations;
int _nextSerialNumber = 0;

std::mutex* accountsMutexes;
std::mutex operationMutex;
std::mutex serialNumberMutex;

std::unordered_map<int, ACCOUNT> readAllAccounts(const std::string& filePath) {
    std::unordered_map<int, ACCOUNT> accounts;
    std::ifstream file(filePath);
    ACCOUNT account;
    while (file >> account.id >> account.balance) {
        account.initialBalance = account.balance;
        accounts[account.id] = account;
    }
    return accounts;
}

void printAllOperations() {
    operationMutex.lock();
    for (auto const& operation : _operations) {
        std::cout << "--> OPERATION serial number: " << operation.serialNumber << "-----" << std::endl;
        std::cout << "source account: " << operation.sourceAccountId << std::endl;
        std::cout << "destination account: " << operation.destinationAccountId << std::endl;
        std::cout << "amount: " << operation.amount << std::endl << std::endl;
    }
    operationMutex.unlock();
}

void printAllAccounts() {
    for (const auto& account : _accounts) {
        std::cout << "Account ID: " << account.first << std::endl;
        std::cout << "Balance: " << account.second.balance << std::endl;
        std::cout << "Initial Balance: " << account.second.initialBalance << std::endl;
        std::cout << "Transaction Log:" << std::endl;
        for (const auto& operation : account.second.log) {
            std::cout << "   OPERATION serial number: " << operation.serialNumber << std::endl;
            std::cout << "   Source account: " << operation.sourceAccountId << std::endl;
            std::cout << "   Destination account: " << operation.destinationAccountId << std::endl;
            std::cout << "   Amount: " << operation.amount << std::endl;
        }
        std::cout << std::endl;
    }
}


int generateRandomNumberInRange(int min, int max) {
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<int> dist(min, max);
    return dist(mt);
}

void createTransaction(OPERATION& operation) {
    if (operation.sourceAccountId < operation.destinationAccountId) {
        accountsMutexes[operation.sourceAccountId].lock();
        accountsMutexes[operation.destinationAccountId].lock();
        if (_accounts[operation.sourceAccountId].balance < operation.amount) {
            accountsMutexes[operation.destinationAccountId].unlock();
            accountsMutexes[operation.sourceAccountId].unlock();
            return;
        }
        serialNumberMutex.lock();
        operation.serialNumber = _nextSerialNumber++;
        _accounts[operation.sourceAccountId].log.push_back(operation);
        serialNumberMutex.unlock();
        _accounts[operation.sourceAccountId].balance -= operation.amount;
        _accounts[operation.destinationAccountId].balance += operation.amount;
        _accounts[operation.destinationAccountId].log.push_back(operation);
        accountsMutexes[operation.sourceAccountId].unlock();
        accountsMutexes[operation.destinationAccountId].unlock();
    }
    else {
        accountsMutexes[operation.destinationAccountId].lock();
        accountsMutexes[operation.sourceAccountId].lock();
        if (_accounts[operation.sourceAccountId].balance < operation.amount) {
            accountsMutexes[operation.sourceAccountId].unlock();
            accountsMutexes[operation.destinationAccountId].unlock();
            return;
        }
        serialNumberMutex.lock();
        operation.serialNumber = _nextSerialNumber++;
        _accounts[operation.destinationAccountId].log.push_back(operation);
        serialNumberMutex.unlock();
        _accounts[operation.destinationAccountId].balance += operation.amount;
        _accounts[operation.sourceAccountId].balance -= operation.amount;
        _accounts[operation.sourceAccountId].log.push_back(operation);
        accountsMutexes[operation.destinationAccountId].unlock();
        accountsMutexes[operation.sourceAccountId].unlock();
    }
    operationMutex.lock();
    _operations.push_back(operation);
    operationMutex.unlock();
}



bool checkIfOperationFromSourceAccountIsInDestinationAccountLog(OPERATION operation) {
    for (auto const& operationFromLog : _accounts[operation.destinationAccountId].log) {
        if (operationFromLog.serialNumber == operation.serialNumber) {
            return true;
        }
    }
    return false;
}

bool checkIfOperationFromDestinationAccountIsInSourceAccountLog(OPERATION operation) {
    for (auto const& operationFromLog : _accounts[operation.sourceAccountId].log) {
        if (operationFromLog.serialNumber == operation.serialNumber) {
            return true;
        }
    }
    return false;
}

void checkConsistency() {
    bool isConsistent = true;
    for (auto const& account : _accounts) {
        accountsMutexes[account.first].lock();
        auto initialBalance = account.second.initialBalance;
        for (auto const& operation : account.second.log) {
            if (operation.sourceAccountId == account.first) {
                initialBalance -= operation.amount;
                isConsistent = checkIfOperationFromSourceAccountIsInDestinationAccountLog(operation);
            }
            else {
                initialBalance += operation.amount;
                isConsistent = checkIfOperationFromDestinationAccountIsInSourceAccountLog(operation);
            }
        }
        if (initialBalance != account.second.balance) {
            isConsistent = false;
            break;
        }
        accountsMutexes[account.first].unlock();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    if (isConsistent) {
        std::cout << "Consistency check passed" << std::endl;
    }
    else {
        std::cout << "Consistency check failed" << std::endl;
    }
}

int main() {
    std::srand(std::time(nullptr));
    _accounts = readAllAccounts(R"(D:\1.School\PDP\Laab1\accounts.txt)");
    accountsMutexes = new std::mutex[_accounts.size()];

    // Create all transactions before starting threads
    std::vector<OPERATION> allTransactions;
    for (int i = 0; i < CREATOR_THREAD_COUNT * TRANSACTIONS_PER_THREAD; i++) {
        OPERATION operation;
        operation.amount = generateRandomNumberInRange(1, 100);
        int senderAccount = generateRandomNumberInRange(0, _accounts.size() - 1);
        int receiverAccount = generateRandomNumberInRange(0, _accounts.size() - 1);
        while (senderAccount == receiverAccount) {
            receiverAccount = generateRandomNumberInRange(0, _accounts.size() - 1);
        }
        operation.sourceAccountId = senderAccount;
        operation.destinationAccountId = receiverAccount;
        allTransactions.push_back(operation);
    }

    auto startTime = std::chrono::high_resolution_clock::now();

    std::thread creatorThreads[CREATOR_THREAD_COUNT];
    for (int i = 0; i < CREATOR_THREAD_COUNT; i++) {
        creatorThreads[i] = std::thread([i, &allTransactions]() {
            for (int j = 0; j < TRANSACTIONS_PER_THREAD; j++) {
                createTransaction(allTransactions[i * TRANSACTIONS_PER_THREAD + j]);
            }
        });
    }

    for (int i = 0; i < CREATOR_THREAD_COUNT; i++) {
        creatorThreads[i].join();
        if (i % 3 == 0) {
            checkConsistency();
        }
    }

    auto endTime = std::chrono::high_resolution_clock::now();

    // Calculate the elapsed time in milliseconds
    auto elapsedTime = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime);

    std::thread printerThread(printAllOperations);
    printerThread.join();

    printAllAccounts();

    std::cout << "Start Time: " << std::chrono::system_clock::to_time_t(std::chrono::system_clock::now()) << std::endl;
    std::cout << "End Time: " << std::chrono::system_clock::to_time_t(std::chrono::system_clock::now()) << std::endl;
    std::cout << "Elapsed Time: " << elapsedTime.count() << " ms" << std::endl;

    delete[] accountsMutexes;
    return 0;

}