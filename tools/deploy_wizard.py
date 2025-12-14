
import os
import subprocess
import time
import webbrowser
import sys

def print_step(title):
    print("\n" + "="*50)
    print(f"🚀 {title}")
    print("="*50 + "\n")

def run_cmd(cmd, cwd=None, ignore_error=False):
    print(f"Running: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True, cwd=cwd)
        return True
    except subprocess.CalledProcessError:
        if not ignore_error:
            print(f"❌ Command failed: {cmd}")
        return False

def check_vercel():
    print_step("Checking prerequisites")
    print("Checking for Vercel CLI...")
    if run_cmd("vercel --version", ignore_error=True):
        print("✅ Vercel CLI found")
        return True
    else:
        print("⚠️ Vercel CLI not found.")
        choice = input("Do you want me to install it? (y/n): ")
        if choice.lower() == 'y':
            print("Installing Vercel CLI (requires Node.js)...")
            if run_cmd("npm install -g vercel"):
                print("✅ Installed Vercel CLI")
                return True
        return False

def git_push():
    print_step("Syncing Code to GitHub")
    print("Preparing to push all changes to GitHub...")
    run_cmd("git add .")
    run_cmd('git commit -m "Prepare for deployment"')
    
    print("\nPushing to remote 'origin'...")
    if run_cmd("git push origin main", ignore_error=True) or run_cmd("git push origin master", ignore_error=True):
        print("✅ Code synced to GitHub")
        return True
    else:
        print("❌ Could not push to GitHub. Make sure you have a remote 'origin' set up.")
        return False

def deploy_backend_render():
    print_step("Backend Deployment (Render)")
    print("1. I have created 'backend/render.yaml' for you.")
    print("2. Go to: https://dashboard.render.com/blueprints")
    print("3. Click 'New Blueprint Instance'")
    print("4. Select your 'autogenesis' repository")
    print("5. Click 'Apply'")
    
    input("\nPress ENTER once you have started the Render deployment...")
    
    backend_url = input("\n🔗 Paste your Render Backend URL here (e.g., https://autogenesis.onrender.com): ").strip()
    while not backend_url.startswith("http"):
        print("❌ Invalid URL. Must start with http:// or https://")
        backend_url = input("🔗 Paste your Render Backend URL here: ").strip()
    
    return backend_url.rstrip("/")

def deploy_frontend_vercel(backend_url):
    print_step("Frontend Deployment (Vercel)")
    
    print(f"Configuring Frontend to talk to: {backend_url}")
    
    # We can pass env vars directly to vercel deploy
    cmd = f'vercel frontend --prod --env NEXT_PUBLIC_API_URL="{backend_url}"'
    
    print("\nStarting Vercel Deployment...")
    print("NOTE: If asked to log in, please follow the browser instructions.")
    print("NOTE: Accept all default settings by pressing Enter.")
    
    run_cmd(cmd, cwd=".")

def main():
    print("""
    Autogenesis Deployment Wizard
    =============================
    I will guide you through deploying:
    1. Backend to Render (via GitHub)
    2. Frontend to Vercel (via CLI)
    """)
    
    if not check_vercel():
        print("❌ Cannot proceed without Vercel CLI.")
        return

    check_git = input("\nIs this project connected to a GitHub repository? (y/n): ")
    if check_git.lower() == 'y':
        if not git_push():
            print("⚠️ Proceeding with local files only (Render requires GitHub though!)")
    
    print("\n--- PHASE 1: BACKEND ---")
    backend_url = deploy_backend_render()
    
    print("\n--- PHASE 2: FRONTEND ---")
    deploy_frontend_vercel(backend_url)
    
    print_step("Deployment Complete!")
    print("Your Autogenesis is live! 🌍")

if __name__ == "__main__":
    main()
