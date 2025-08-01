<<<<<<< HEAD
import subprocess

def is_git_connected():
    try:
        # Check if inside a Git repository
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Check if a remote named 'origin' exists
        result = subprocess.run(["git", "remote"], capture_output=True, text=True)
        return "origin" in result.stdout.strip()
    except subprocess.CalledProcessError:
        return False

# This will always print the result when run locally (in VS Code)
if __name__ == "__main__":
    if not is_git_connected():
        print("❌ ERROR: Git is not connected to a remote repository. Skipping deployment.")
    else:
        print("✅ Git is connected. You may deploy.")
    
    # Run palindrome check locally for testing
    word = "madam"  # Example input
    if word == word[::-1]:
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is not a palindrome")

# AWS Lambda entry point
def lambda_handler(event=None, context=None):
    word = "madam"  # Example input
    if word == word[::-1]:
        return {
            "statusCode": 200,
            "body": f"'{word}' is a palindrome"
        }
    else:
        return {
            "statusCode": 200,
            "body": f"'{word}' is not a palindrome"
        }
=======
def lambda_handler(event, context):
    a = 10
    b = 15
    result = a + b
    
    return {
        'statusCode': 200,
        'body': f'The sum of {a} and {b} is {result}'
    }
>>>>>>> 6790e5abd873d1034cdc1380e05af4b4756d5866
