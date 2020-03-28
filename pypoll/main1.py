import csv

input_file = "election_data.csv"
output_file = "election_results.txt"


#set variables for calculations and code
total_votes = 0

#set lists
candidates = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#You will be give a set of poll data called election_data.csv. 
with open(input_file) as election_data:
    reader = csv.DictReader(election_data)
    for row in reader:

    #The dataset is composed of three columns: Voter ID, County, and Candidate.
    #Your task is to create a Python script that analyzes the votes and 
    #calculates each of the following:

    #The total number of votes cast
        total_votes = total_votes + 1

        #A complete list of candidates who received votes
        candidate_name = row["Candidate"]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1



with open(output_file, "w") as text_file:
    election_results = (
    f"\nElection Results\n"
    f"---------------------------------\n"
    f"Total Votes:{total_votes}\n"
    f"---------------------------------\n")

    print(election_results)
    text_file.write(election_results)
    #The percentage of votes each candidate won
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        text_file.write(voter_output)


#The winner of the election based on popular vote.
    winning_candidate_results = (
    f"\nElection Results\n"
    f"---------------------------------\n"
    f"Winner:{winning_candidate}\n"
    f"---------------------------------\n")

    print(winning_candidate_results)
    text_file.write(winning_candidate_results)

#As an example, your analysis should look similar to the one below:




