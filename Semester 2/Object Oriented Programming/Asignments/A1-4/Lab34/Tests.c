#include "Tests.h"
#include "assert.h"

void testProfile()
{
	char testId[] = "1";
	char testPlaceOfBirth[] = "New York";
	char testPsychologicalProfile[] = "abcd";
	int yearsOfService = 3;
	Profile *testProfile = createProfile(testId,testPlaceOfBirth,testPsychologicalProfile,yearsOfService);
	assert(strcmp(getID(testProfile), "1") == 0);
	assert(getYearsOfRecordedService(testProfile) == 3);
	testProfile->yearsOfRecordedService = 5;
	assert(getYearsOfRecordedService(testProfile) == 5);
	destroyProfile(testProfile);
}

void testAdd()
{
	DynamicArray *testRepository = createArray(1,&destroyProfile,&copyProfile);
	assert(addProfile(testRepository, "1", "a", "b", 1)==1);
	assert(getYearsOfRecordedService(testRepository->elements[0]) == 1);
	assert(addProfile(testRepository, "1", "a", "b", 1) == -1);
	destroyArray(testRepository);
}

void testUpdate()
{
	DynamicArray *testRepository = createArray(1, &destroyProfile, &copyProfile);
	assert(addProfile(testRepository, "1", "a", "b", 1) == 1);
	assert(updateProfile(testRepository, "1", "c", "c", 3) == 1);
	assert(getYearsOfRecordedService(testRepository->elements[0]) == 3);
	assert(updateProfile(testRepository, "2", "c", "c", 3) == -1);
	destroyArray(testRepository);
}

void testDelete()
{
	DynamicArray *testRepository = createArray(1, &destroyProfile, &copyProfile);
	assert(addProfile(testRepository, "1", "a", "b", 1) == 1);
	assert(deleteProfile(testRepository, "1") == 1);
	assert(deleteProfile(testRepository, "1") == -1);
	destroyArray(testRepository);
}

void testList()
{
	DynamicArray *testRepository = createArray(1, &destroyProfile, &copyProfile);
	assert(addProfile(testRepository, "1", "a", "b", 1) == 1);
	char testOutput[21];
	testOutput[0] = 0;
	listProfiles(testRepository, testOutput);
	assert(strcmp(testOutput, "1 a b 1\n") == 0);
	assert(addProfile(testRepository, "2", "a", "b", 1) == 1);
	testOutput[0] = 0;
	listProfilesByPsychologicalProfile(testRepository, "b", testOutput);
	assert(strcmp(testOutput, "1 a b 1\n2 a b 1\n") == 0);
	destroyArray(testRepository);
}

void runTests()
{
	testProfile();
	testAdd();
	testUpdate();
	testDelete();
	testList();
}
