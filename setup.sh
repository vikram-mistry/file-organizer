#!/bin/bash

echo "Checking Python version..."
python3 --version

echo "Upgrading pip, setuptools, and wheel..."
python3 -m pip install --upgrade pip setuptools wheel --user

if [ -f requirements.txt ]; then
  echo "Installing dependencies from requirements.txt..."
  python3 -m pip install -r requirements.txt --user
else
  echo "No requirements.txt found, skipping dependency installation."
fi

# Dynamically get the user base binary directory
PIP_USER_BIN="$(python3 -m site --user-base)/bin"

# Add pip user bin folder to PATH if not already present
if ! grep -q "export PATH=$PIP_USER_BIN:\$PATH" ~/.zshrc; then
  echo "Adding pip user bin folder to PATH in ~/.zshrc"
  echo "export PATH=$PIP_USER_BIN:\$PATH" >> ~/.zshrc
  echo "Reloading shell configuration..."
  source ~/.zshrc
else
  echo "Pip user bin folder already in PATH"
fi

echo "Setup complete! You can now run the script as:"
echo "file-organizer /path/to/folder"