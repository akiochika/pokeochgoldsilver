import base64  # これを追加

# GitHubのリポジトリ情報を設定
GITHUB_REPO = "akiochika/pokeochgoldsilver"  # 例: "username/repository"

def get_file_sha(file_path):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{file_path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["sha"]
    return None

def update_github_file(file_path, content):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{file_path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    file_sha = get_file_sha(file_path)
    data = {
        "message": f"Update {file_path}",
        "content": base64.b64encode(content.encode()).decode(),
        "sha": file_sha
    }
    response = requests.put(url, headers=headers, json=data)
    
    # ログの追加
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    print(f"Data: {data}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    if response.status_code == 200:
        print(f"Successfully updated {file_path} on GitHub")
    else:
        print(f"Failed to update {file_path} on GitHub: {response.content}")
