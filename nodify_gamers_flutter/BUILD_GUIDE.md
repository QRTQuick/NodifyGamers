# 🚀 NodifyGamers Flutter - Git Workflow & Build Guide

## Overview
This guide explains how to set up automated APK builds using GitHub Actions and answers whether you need any APIs.

---

## 📋 Do You Need Any API?

**Short Answer: NO** - You don't need any external API to compile your Flutter app to APK.

**What's Included:**
- ✅ **Flutter SDK** - Installed automatically by GitHub Actions
- ✅ **Java JDK** - Installed automatically for Android builds
- ✅ **Android SDK** - Pre-installed on GitHub runners
- ✅ **Gradle** - Included with Android build tools

**When You MIGHT Need APIs:**
- 📱 **Google Play Store Upload** - Only if you want to auto-publish to Play Store (requires Google Play Developer API)
- 🔔 **Push Notifications** - If implementing Firebase Cloud Messaging
- 🗺️ **Maps/Location** - If adding Google Maps integration
- 🎮 **Game APIs** - For fetching game data from external sources (Steam API, IGDB, etc.)

For **basic APK compilation**, no external APIs are needed!

---

## 🔧 GitHub Actions Workflow Setup

### Files Created:
```
.github/
  workflows/
    build-android.yml    # Automated APK/AAB build pipeline
```

### How It Works:

#### 1. **On Every Push/PR** to `main` or `master`:
   - ✅ Checks out code
   - ✅ Sets up Java 17 & Flutter 3.24
   - ✅ Installs dependencies (`flutter pub get`)
   - ✅ Runs tests (if available)
   - ✅ Analyzes code (`flutter analyze`)
   - ✅ Builds **debug APK** (if no keystore) or **signed release APK** (if keystore provided)
   - ✅ Uploads APK as artifact (downloadable for 30 days)

#### 2. **On Version Tags** (e.g., `v1.0.0`, `v2.1.3`):
   - ✅ Does everything above
   - ✅ Builds **Release APK** (signed if keystore available)
   - ✅ Builds **Android App Bundle (AAB)** for Play Store
   - ✅ Creates a **GitHub Release** with APK & AAB attached
   - ✅ Auto-generates release notes from commits

---

## 🔐 Setting Up Signed Releases (Optional)

To create **signed release APKs** instead of debug builds:

### Step 1: Generate a Keystore
```bash
keytool -genkey -v -keystore key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias key
```

### Step 2: Encode Keystore to Base64
```bash
# Linux/Mac
base64 key.jks | tr -d '\n'

# Windows (PowerShell)
[Convert]::ToBase64String([IO.File]::ReadAllBytes("key.jks"))
```

### Step 3: Add GitHub Secrets
Go to your repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**:

| Secret Name | Value |
|-------------|-------|
| `ANDROID_KEYSTORE_BASE64` | Paste the base64 string from Step 2 |
| `ANDROID_STORE_PASSWORD` | Your keystore password |
| `ANDROID_KEY_PASSWORD` | Your key password |
| `ANDROID_KEY_ALIAS` | Your key alias (e.g., `key`) |

### Step 4: Create a Release Tag
```bash
git tag v1.0.0
git push origin v1.0.0
```

This triggers the full release pipeline with signed APK + AAB!

---

## 📥 Downloading Built APKs

### From Pull Request / Push:
1. Go to the **Actions** tab in your GitHub repo
2. Click on the workflow run
3. Scroll to **Artifacts** section
4. Click `app-apk` to download

### From Release:
1. Go to **Releases** in your GitHub repo
2. Find the version tag (e.g., v1.0.0)
3. Download APK or AAB from **Assets**

---

## 🏗️ Manual Build Commands (Local Development)

If you prefer building locally:

### Debug APK (for testing):
```bash
cd nodify_gamers_flutter
flutter build apk --debug
# Output: build/app/outputs/flutter-apk/debug/app-debug.apk
```

### Release APK (unsigned):
```bash
flutter build apk --release
# Output: build/app/outputs/flutter-apk/release/app-release.apk
```

### Signed Release APK (requires keystore):
```bash
# Configure android/key.properties first
flutter build apk --release
```

### App Bundle (for Play Store):
```bash
flutter build appbundle --release
# Output: build/app/outputs/bundle/release/app-release.aab
```

---

## 📊 Workflow Summary Table

| Trigger | APK Type | AAB | GitHub Release | Requires Secrets |
|---------|----------|-----|----------------|------------------|
| Push to main | Debug (or Signed*) | ❌ | ❌ | Optional |
| Pull Request | Debug | ❌ | ❌ | No |
| Tag (v*) | Signed* | ✅ | ✅ | Recommended |

*\*Signed if secrets are configured, otherwise unsigned/debug*

---

## 🛠️ Troubleshooting

### Build Fails with "SDK not found"
- GitHub Actions includes Android SDK by default
- Ensure you're using `ubuntu-latest` runner

### APK Too Large
- Enable code shrinking in `android/app/build.gradle`:
```gradle
buildTypes {
    release {
        shrinkResources true
        minifyEnabled true
    }
}
```

### Want to Auto-Publish to Play Store?
Add this job to the workflow (requires Google Play API credentials):
```yaml
publish-to-play-store:
  needs: build-appbundle
  runs-on: ubuntu-latest
  steps:
    - uses: actions/upload-artifact@v4
      with:
        name: app-aab
    - uses: r0adkll/upload-google-play@v1
      with:
        serviceAccountJsonPlainText: ${{ secrets.GOOGLE_PLAY_SERVICE_ACCOUNT }}
        packageName: com.nodifygamers.app
        releaseFiles: build/app/outputs/bundle/release/*.aab
        track: internal
```

---

## 🎯 Next Steps

1. ✅ **Commit the workflow file** to your repository
2. ✅ **Push to GitHub** - Actions will run automatically
3. ✅ **(Optional)** Configure secrets for signed releases
4. ✅ **Create a tag** to test the full release pipeline
5. ✅ **Download your APK** from Actions or Releases

---

## 📞 Support

For issues:
- Check **Actions** tab for build logs
- Review Flutter's [Android deployment docs](https://docs.flutter.dev/deployment/android)
- Ensure `android/` folder exists (run `flutter create .` if missing)

**Happy Building! 🚀**
