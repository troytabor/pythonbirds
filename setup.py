import os
import subprocess
import sys

def create_venv():
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
    else:
        print("Virtual environment already exists.")

def install_packages():
    print("Installing packages...")
    subprocess.check_call([
        os.path.join('venv', 'Scripts' if os.name == 'nt' else 'bin', 'python'),
        '-m', 'pip', 'install', 'pandas', 'matplotlib', 'plotly', 'flask', 'geopy', 'us'
    ])

def main():
    create_venv()
    install_packages()
    print("Setup complete!")

if __name__ == '__main__':
    main()
