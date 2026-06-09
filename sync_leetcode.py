import requests

USERNAME = "mohamedellithyyy"

URL = "https://leetcode.com/graphql"

QUERY = """
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    submitStats: submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""

def fetch_stats():
    r = requests.post(URL, json={
        "query": QUERY,
        "variables": {"username": USERNAME}
    })

    data = r.json()["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

    stats = {"Easy": 0, "Medium": 0, "Hard": 0, "All": 0}

    for item in data:
        stats[item["difficulty"]] = item["count"]

    return stats


if __name__ == "__main__":
    print(fetch_stats())