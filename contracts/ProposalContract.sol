// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract ProposalContract {
    struct Proposal {
        uint id;
        string title;
        string summary;
        address proposer;
        uint voteYes;
        uint voteNo;
        bool executed;
        uint timestamp;
    }

    uint public proposalCounter;
    mapping(uint => Proposal) public proposals;
    mapping(uint => mapping(address => bool)) public hasVoted;

    event ProposalSubmitted(uint indexed id, address indexed proposer, string title);
    event Voted(uint indexed id, address indexed voter, bool support);
    event ProposalExecuted(uint indexed id, bool accepted);

    modifier proposalExists(uint _id) {
        require(_id < proposalCounter, "Proposal does not exist.");
        _;
    }

    function submitProposal(string memory _title, string memory _summary) public {
        Proposal storage p = proposals[proposalCounter];
        p.id = proposalCounter;
        p.title = _title;
        p.summary = _summary;
        p.proposer = msg.sender;
        p.timestamp = block.timestamp;

        emit ProposalSubmitted(proposalCounter, msg.sender, _title);
        proposalCounter++;
    }

    function vote(uint _id, bool support) public proposalExists(_id) {
        require(!hasVoted[_id][msg.sender], "You have already voted.");

        if (support) {
            proposals[_id].voteYes++;
        } else {
            proposals[_id].voteNo++;
        }

        hasVoted[_id][msg.sender] = true;
        emit Voted(_id, msg.sender, support);
    }

    function executeProposal(uint _id) public proposalExists(_id) {
        Proposal storage p = proposals[_id];
        require(!p.executed, "Already executed.");

        p.executed = true;
        bool accepted = p.voteYes > p.voteNo;

        emit ProposalExecuted(_id, accepted);
    }

    function getProposal(uint _id) public view proposalExists(_id) returns (
        string memory title,
        string memory summary,
        address proposer,
        uint voteYes,
        uint voteNo,
        bool executed,
        uint timestamp
    ) {
        Proposal storage p = proposals[_id];
        return (p.title, p.summary, p.proposer, p.voteYes, p.voteNo, p.executed, p.timestamp);
    }
}