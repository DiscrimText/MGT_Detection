import gdown
import os
import argparse

# === Argument Parser ===
parser = argparse.ArgumentParser(description='Download a file from Google Drive.')
parser.add_argument('--output_dir', type=str, required=True, help='Output folder path')
args = parser.parse_args()

# === Google Drive Config ===
url = 'https://drive.google.com/file/d/14HJJzGIT5aQDSpQ6l96k1iYUdDZIEe5R/view?usp=sharing'
file_id = url.split('/d/')[1].split('/')[0]
download_url = f'https://drive.google.com/uc?id={file_id}'

# Create output directory
os.makedirs(args.output_dir, exist_ok=True)

# Output file path
output_file = os.path.join(args.output_dir, 'downloaded_file.ext')

# Download
gdown.download(download_url, output_file, quiet=False)

print(f'✅ File downloaded to: {output_file}')
