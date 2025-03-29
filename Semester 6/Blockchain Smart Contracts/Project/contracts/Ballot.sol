// SPDX-License-Identifier: MIT

// Run project in Etherum Remix IDE, complile contract and then access it

pragma solidity >= 0.7.0<0.9.0;
// making a voring contract

// 1. we want the ability to accept proposals and store them
// proposal: their name, number

// 2. voters & voting ability
// keep track of voting
// check voters are authenticated to vote

// 3. chairman
// authenticate and deploy contract

contract Ballot {

    // voters: vote index = uint, voted = bool, access to vode = uint
    struct Voter {
        uint vote;
        bool voted;
        uint weight;
    }

    struct Proposal {

    // use bytes32 instead of string to save gas and make a more efficient code
    string name; // name of proposal
    uint voteCount; // nr of accumulated votes

    }

    Proposal[] public proposals;

    // mapping allows us to create a store store value with keys and indexes

    mapping(address => Voter) public voters; // voters get address as a key and Voter for value

    address public chairman;

    constructor(string[] memory proposalNames) {
        // memory defines a temporary data location in Solidity during runtime only of methods
        // we guarantee space for it

        // msg.sender = is a global variable that states who 
        // is currentlyl connecting to the contract

        chairman = msg.sender;
        voters[chairman].weight = 1;

        // add proposal names to the smart contract upon deployment
        for(uint i=0; i< proposalNames.length; i++) {
            proposals.push(Proposal({
                name: proposalNames[i],
                voteCount: 0
            }));
        }
    }

    // authenticating voter
    function giveRightToVote(address voter) public {
        require(msg.sender == chairman, "Only the chairman can give access to vote");
        // require that the voter hasnt voted yet
        require(!voters[voter].voted, "User has already voted");
        require(voters[voter].weight == 0);
        voters[voter].weight =1;
    }

    // voting
    function vote(uint proposal) public {
        Voter storage sender = voters[msg.sender];
        require(sender.weight != 0, "Has no right to vote");
        require(!sender.voted, "Already voted");
        sender.voted = true;
        sender.vote = proposal;

        proposals[proposal].voteCount += sender.weight;
    }

    // functions for showing the results

    // show the winning proposal by integer
    function winningProposal() public view returns (uint winningProposal_) {

        uint winningVoteCount = 0;
        for(uint i = 0; i < proposals.length; i++) {
            if(proposals[i].voteCount > winningVoteCount) {
                winningVoteCount = proposals[i].voteCount;
                winningProposal_ = i;
            }
        }
    }

    // shows the winner by name
    function winningName() public view returns  (string memory winningName_) {
        winningName_ = proposals[winningProposal()].name;
    }
}