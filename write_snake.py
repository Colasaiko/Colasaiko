content = """name: Generate Snake

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Generate Snake Animation
        uses: Platane/snk@v3
        with:
          github_user_name: Colasaiko
          outputs: |
            dist/github-snake.svg?color_snake=#62574C&color_dots=#F7F3EA,#F1E8D8,#E5D5BD,#B89B72,#8A735B
            dist/github-snake-dark.svg?palette=github-dark&color_snake=#B89B72

      - name: Push to Output Branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
"""
with open('.github/workflows/snake.yml', 'w', encoding='utf-8') as f:
    f.write(content)
