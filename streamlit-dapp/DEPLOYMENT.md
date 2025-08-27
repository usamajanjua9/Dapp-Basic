# 🚀 Deploy to Streamlit Cloud

This guide will help you deploy your Simple DApp to Streamlit Cloud for free!

## 📋 Prerequisites

1. **GitHub Account** - You'll need a GitHub account
2. **Streamlit Account** - Sign up at [share.streamlit.io](https://share.streamlit.io)
3. **Your Code** - Make sure your code is in a GitHub repository

## 🎯 Step-by-Step Deployment

### 1. Push to GitHub

```bash
# Initialize git repository (if not already done)
git init
git add .
git commit -m "Initial commit: Simple DApp with wallet functionality"

# Add your GitHub remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### 2. Deploy on Streamlit Cloud

1. **Go to [share.streamlit.io](https://share.streamlit.io)**
2. **Sign in with GitHub**
3. **Click "New app"**
4. **Fill in the details:**
   - **Repository**: Select your repository
   - **Branch**: `main` (or your default branch)
   - **Main file path**: `app.py`
   - **App URL**: Choose a custom URL (optional)
5. **Click "Deploy"**

### 3. Wait for Deployment

- Streamlit will automatically install dependencies from `requirements.txt`
- The first deployment might take 2-3 minutes
- You'll see a success message when done

## 🔧 Configuration

Your app already includes:
- ✅ `requirements.txt` - Dependencies
- ✅ `.streamlit/config.toml` - Theme and server settings
- ✅ `app.py` - Main application

## 🌐 Access Your App

Once deployed, your app will be available at:
```
https://YOUR_APP_NAME-YOUR_USERNAME.streamlit.app
```

## 📱 Features Available After Deployment

- **Wallet Connect/Disconnect** - Fully functional
- **Responsive Design** - Works on all devices
- **Beautiful UI** - Custom theme applied
- **Multiple Sections** - Navigation between features
- **Session Management** - State persistence

## 🔄 Updating Your App

1. **Make changes to your code**
2. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Update: [describe your changes]"
   git push
   ```
3. **Streamlit Cloud automatically redeploys** within minutes

## 🐛 Troubleshooting

### Common Issues:

1. **Import Errors**: Make sure all packages are in `requirements.txt`
2. **Deployment Fails**: Check the deployment logs in Streamlit Cloud
3. **App Not Loading**: Verify the main file path is correct

### Check Logs:

- Go to your app in Streamlit Cloud
- Click the three dots menu → "View app logs"
- Look for error messages

## 🎉 Success!

Your Simple DApp is now live on the internet! Share the URL with others to show off your Web3 application.

## 🔗 Useful Links

- [Streamlit Cloud](https://share.streamlit.io)
- [Streamlit Documentation](https://docs.streamlit.io)
- [GitHub](https://github.com)

---

**Happy Deploying! 🚀**
