name: Bot Workflow

on:
  push:
    branches:
      - main
  schedule:
    - cron: 0 */12 * * *

jobs:
  run-bot:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Setup environment
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run bot
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
        run: |
          python bot.py
