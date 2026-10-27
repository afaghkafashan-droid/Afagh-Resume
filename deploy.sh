#!/usr/bin/env bash
# ساخت و استقرار سایت روی Cloudflare Pages
# استفاده:  CLOUDFLARE_API_TOKEN=توکنت ./deploy.sh
set -e

cd "$(dirname "$0")"

echo "▶ Building site..."
python build.py

echo "▶ Deploying to Cloudflare Pages..."
npx wrangler pages deploy output --project-name=kfnafagh --branch=main

echo "✅ Done! Live at https://kfnafagh.pages.dev"
