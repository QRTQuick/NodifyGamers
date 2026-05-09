import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/settings_provider.dart';
import '../utils/theme.dart';

/// Settings screen with categorized options
class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer<SettingsProvider>(
      builder: (context, settingsProvider, child) {
        return SingleChildScrollView(
          padding: const EdgeInsets.all(30),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Header
              _buildHeader(),
              const SizedBox(height: 25),
              
              // Settings sections
              _buildGeneralSection(settingsProvider),
              const SizedBox(height: 25),
              _buildAppearanceSection(settingsProvider),
              const SizedBox(height: 25),
              _buildDownloadsSection(settingsProvider),
              const SizedBox(height: 25),
              _buildNotificationsSection(settingsProvider),
              const SizedBox(height: 30),
              
              // Save button
              Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  ElevatedButton.icon(
                    onPressed: () {},
                    icon: const Icon(Icons.save),
                    label: const Text('Save Changes'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppTheme.primary,
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(
                        horizontal: 24,
                        vertical: 14,
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildHeader() {
    return Container(
      padding: const EdgeInsets.only(bottom: 15),
      decoration: BoxDecoration(
        border: Border(
          bottom: BorderSide(
            color: const Color(0xFF334155),
            width: 1,
          ),
        ),
      ),
      child: Row(
        children: [
          const Expanded(
            child: Text(
              'Settings',
              style: TextStyle(
                color: AppTheme.textPrimary,
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildGeneralSection(SettingsProvider provider) {
    return _SettingsSection(
      title: '⚙️ General',
      children: [
        _SettingRow(
          title: 'Language',
          description: 'Select your preferred language',
          child: Container(
            width: 200,
            decoration: BoxDecoration(
              color: AppTheme.surface,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: AppTheme.surfaceLight),
            ),
            child: DropdownButtonHideUnderline(
              child: DropdownButton<String>(
                value: provider.language,
                isExpanded: true,
                dropdownColor: AppTheme.surface,
                items: ['English', 'Spanish', 'French', 'German', 'Japanese']
                    .map((lang) => DropdownMenuItem(
                          value: lang,
                          child: Text(
                            lang,
                            style: const TextStyle(color: AppTheme.textPrimary),
                          ),
                        ))
                    .toList(),
                onChanged: (value) {
                  if (value != null) provider.setLanguage(value);
                },
              ),
            ),
          ),
        ),
        _SettingRow(
          title: 'Launch on Startup',
          description: 'Start NodifyGamers when Windows starts',
          child: Switch(
            value: provider.launchOnStartup,
            onChanged: (value) => provider.setLaunchOnStartup(value),
          ),
        ),
        _SettingRow(
          title: 'Run in Background',
          description: 'Keep app running when closed',
          child: Switch(
            value: provider.runInBackground,
            onChanged: (value) => provider.setRunInBackground(value),
          ),
        ),
      ],
    );
  }

  Widget _buildAppearanceSection(SettingsProvider provider) {
    return _SettingsSection(
      title: '🎨 Appearance',
      children: [
        _SettingRow(
          title: 'Theme',
          description: 'Choose application theme',
          child: Container(
            width: 200,
            decoration: BoxDecoration(
              color: AppTheme.surface,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: AppTheme.surfaceLight),
            ),
            child: DropdownButtonHideUnderline(
              child: DropdownButton<String>(
                value: provider.theme,
                isExpanded: true,
                dropdownColor: AppTheme.surface,
                items: ['Dark Mode', 'Light Mode', 'Auto']
                    .map((theme) => DropdownMenuItem(
                          value: theme,
                          child: Text(
                            theme,
                            style: const TextStyle(color: AppTheme.textPrimary),
                          ),
                        ))
                    .toList(),
                onChanged: (value) {
                  if (value != null) provider.setTheme(value);
                },
              ),
            ),
          ),
        ),
        _SettingRow(
          title: 'Accent Color',
          description: 'Customize accent color',
          child: Container(
            width: 200,
            decoration: BoxDecoration(
              color: AppTheme.surface,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: AppTheme.surfaceLight),
            ),
            child: DropdownButtonHideUnderline(
              child: DropdownButton<String>(
                value: provider.accentColor,
                isExpanded: true,
                dropdownColor: AppTheme.surface,
                items: ['Purple', 'Blue', 'Green', 'Orange', 'Pink']
                    .map((color) => DropdownMenuItem(
                          value: color,
                          child: Text(
                            color,
                            style: const TextStyle(color: AppTheme.textPrimary),
                          ),
                        ))
                    .toList(),
                onChanged: (value) {
                  if (value != null) provider.setAccentColor(value);
                },
              ),
            ),
          ),
        ),
        _SettingRow(
          title: 'Enable Animations',
          description: 'Smooth transitions and effects',
          child: Switch(
            value: provider.enableAnimations,
            onChanged: (value) => provider.setEnableAnimations(value),
          ),
        ),
      ],
    );
  }

  Widget _buildDownloadsSection(SettingsProvider provider) {
    return _SettingsSection(
      title: '⬇️ Downloads',
      children: [
        _SettingRow(
          title: 'Download Location',
          description: provider.downloadLocation,
          child: ElevatedButton.icon(
            onPressed: () {},
            icon: const Icon(Icons.folder),
            label: const Text('Browse...'),
            style: ElevatedButton.styleFrom(
              backgroundColor: AppTheme.surfaceLight,
              foregroundColor: Colors.white,
            ),
          ),
        ),
        _SettingRow(
          title: 'Auto-Update Games',
          description: 'Automatically download updates',
          child: Switch(
            value: provider.autoUpdateGames,
            onChanged: (value) => provider.setAutoUpdateGames(value),
          ),
        ),
        _SettingRow(
          title: 'Download Speed Limit',
          description: 'Current: ${provider.downloadSpeedLimit}%',
          child: SizedBox(
            width: 200,
            child: Slider(
              value: provider.downloadSpeedLimit.toDouble(),
              min: 0,
              max: 100,
              divisions: 10,
              onChanged: (value) {
                provider.setDownloadSpeedLimit(value.toInt());
              },
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildNotificationsSection(SettingsProvider provider) {
    return _SettingsSection(
      title: '🔔 Notifications',
      children: [
        _SettingRow(
          title: 'Update Notifications',
          description: 'Get notified when updates are available',
          child: Switch(
            value: provider.updateNotifications,
            onChanged: (value) => provider.setUpdateNotifications(value),
          ),
        ),
        _SettingRow(
          title: 'News & Promotions',
          description: 'Receive news and promotional content',
          child: Switch(
            value: provider.newsNotifications,
            onChanged: (value) => provider.setNewsNotifications(value),
          ),
        ),
        _SettingRow(
          title: 'Desktop Notifications',
          description: 'Show popup notifications',
          child: Switch(
            value: provider.desktopNotifications,
            onChanged: (value) => provider.setDesktopNotifications(value),
          ),
        ),
      ],
    );
  }
}

/// Settings Section Widget
class _SettingsSection extends StatelessWidget {
  final String title;
  final List<Widget> children;

  const _SettingsSection({required this.title, required this.children});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            title,
            style: const TextStyle(
              color: AppTheme.primary,
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 15),
          ...children,
        ],
      ),
    );
  }
}

/// Setting Row Widget
class _SettingRow extends StatelessWidget {
  final String title;
  final String description;
  final Widget child;

  const _SettingRow({
    required this.title,
    required this.description,
    required this.child,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 12),
      child: Row(
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(
                    color: AppTheme.textPrimary,
                    fontWeight: FontWeight.w600,
                    fontSize: 15,
                  ),
                ),
                const SizedBox(height: 3),
                Text(
                  description,
                  style: TextStyle(
                    color: AppTheme.textSecondary,
                    fontSize: 13,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 20),
          child,
        ],
      ),
    );
  }
}
