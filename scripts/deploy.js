async function main() {
  const ProposalContract = await ethers.getContractFactory("ProposalContract");
  const contract = await ProposalContract.deploy();
  await contract.deployed();
  console.log("ProposalContract deployed to:", contract.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});