import os
import csv

os.chdir(os.path.dirname(__file__))
poll_data_csv_path = os.path.join("Resources", "election_data.csv")

candidate = []
votes = []
name = []

with open(poll_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    for row in csv_reader:
        candidate.append(row[2])

    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]
    
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)
    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       
            
total_votes = len(candidate)
correy_total = candidate.count("Correy")
correy_percent = int(correy_total) / int(total_votes)
o_tooley_total = candidate.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes
li_total = candidate.count("Li")
li_percent = li_total / total_votes
khan_total = candidate.count("Khan")
khan_percent = khan_total / total_votes

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Khan: {khan_percent:.3%} ({khan_total})")
print(f"Correy: {correy_percent:.3%} ({correy_total})")
print(f"Li: {li_percent:.3%} ({li_total})")
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print(f"-------------------------")
print(f"Winner: {winner_name}")
print(f"-------------------------")

poll_file = os.path.join("Analysis/poll_data.txt")
with open(poll_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Khan: {khan_percent:.3%} ({khan_total})\n")
    outfile.write(f"Correy: {correy_percent:.3%} ({correy_total})\n")
    outfile.write(f"Li: {li_percent:.3%} ({li_total})\n")
    outfile.write(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner_name}\n")
    outfile.write(f"-------------------------\n")