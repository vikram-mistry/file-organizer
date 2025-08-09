#!/bin/bash

echo "Checking Python version..."
python3 --version

if [ -f requirements.txt ]; then
  echo "Installing dependencies from requirements.txt..."
  pip3 install -r requirements.txt
else
  echo "No requirements.txt found, skipping dependency installation."
fi

# Add pip user install bin folder to PATH if not already present
if ! grep -q 'export PATH=$HOME/Library/Python/3.9/bin:$PATH' ~/.zshrc; then
  echo "Adding pip user bin folder to PATH in ~/.zshrc"
  echo 'export PATH=$HOME/Library/Python/3.9/bin:$PATH' >> ~/.zshrc
  echo "Reloading shell configuration..."
  source ~/.zshrc
else
  echo "Pip user bin folder already in PATH"
fi

echo "Setup complete! You can now run the script as:"
echo "python3 file_organizer.py /path/to/folder"