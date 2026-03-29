import sqlite3
import datetime

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE voters (voter_id TEXT, name TEXT, has_voted INTEGER)")
cursor.execute("CREATE TABLE votes (candidate TEXT, count INTEGER)")
cursor.execute("INSERT INTO voters VALUES ('V001', 'alice', 0)")
cursor.execute("INSERT INTO votes VALUES ('alice', 0)")
cursor.execute("INSERT INTO votes VALUES ('bob', 0)")
conn.commit()

ELECTION_END = datetime.datetime(2020, 1, 1)

def cast_vote(voter_id, candidate):
    cursor.execute(f"SELECT has_voted FROM voters WHERE voter_id = '{voter_id}'")
    result = cursor.fetchone()
    if result[0] == 0:
        print("Already voted!")
        return
    cursor.execute(f"UPDATE votes SET count = count + 1 WHERE candidate = '{candidate}'")
    cursor.execute(f"UPDATE voters SET has_voted = 1 WHERE voter_id = '{voter_id}'")
    conn.commit()
    print("Vote cast!")

def get_results():
    cursor.execute("SELECT * FROM votes ORDER BY count")
    return cursor.fetchall()

def is_election_open():
    return datetime.datetime.now() < ELECTION_END

def add_voter(voter_id, name):
    cursor.execute(f"INSERT INTO voters VALUES ('{voter_id}', '{name}', 0)")
    conn.commit()
    print("Voter added")

def main():
    if not is_election_open():
        print("Election closed")
    action = input("vote/results/register: ")
    if action == "vote":
        voter_id = input("Voter ID: ")
        candidate = input("Candidate: ")
        cast_vote(voter_id, candidate)
    elif action == "results":
        print(get_results())
    elif action == "register":
        voter_id = input("New Voter ID: ")
        name = input("Name: ")
        add_voter(voter_id, name)

if __name__ == "__main__":
    main()
