import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/games_provider.dart';
import '../providers/app_provider.dart';
import '../utils/theme.dart';

/// Dashboard screen with statistics, quick actions, and activity feed
class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer2<AppProvider, GamesProvider>(
      builder: (context, appProvider, gamesProvider, child) {
        return SingleChildScrollView(
          padding: const EdgeInsets.all(30),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Header
              _buildHeader(),
              const SizedBox(height: 30),
              
              // Statistics Grid
              _buildStatsGrid(gamesProvider),
              const SizedBox(height: 30),
              
              // Quick Actions & Activity Feed
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Quick Actions
                  Expanded(
                    flex: 1,
                    child: _buildQuickActions(context),
                  ),
                  const SizedBox(width: 25),
                  // Activity Feed
                  Expanded(
                    flex: 2,
                    child: _buildActivityFeed(),
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
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'Welcome back, Gamer! 👋',
                style: TextStyle(
                  color: AppTheme.textPrimary,
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 5),
              Text(
                'Here\'s what\'s happening with your games',
                style: TextStyle(
                  color: AppTheme.textSecondary,
                  fontSize: 14,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildStatsGrid(GamesProvider gamesProvider) {
    final stats = [
      ('Total Games', gamesProvider.totalGames.toString(), '🎯', AppTheme.primary),
      ('Playing Now', '3', '🎮', AppTheme.secondary),
      ('Updates Available', gamesProvider.updatesAvailable.toString(), '⬇️', AppTheme.accent),
      ('Achievements', '142', '🏆', const Color(0xFFEC4899)),
    ];

    return GridView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        mainAxisSpacing: 20,
        crossAxisSpacing: 20,
        childAspectRatio: 1.6,
      ),
      itemCount: stats.length,
      itemBuilder: (context, index) {
        final stat = stats[index];
        return _StatCard(
          title: stat.$1,
          value: stat.$2,
          icon: stat.$3,
          color: stat.$4,
        );
      },
    );
  }

  Widget _buildQuickActions(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            'Quick Actions',
            style: TextStyle(
              color: AppTheme.textPrimary,
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 15),
          Wrap(
            spacing: 15,
            runSpacing: 15,
            children: [
              _QuickActionBtn(
                icon: '➕',
                text: 'Add Game',
                onTap: () => context.read<AppProvider>().navigateTo(1),
              ),
              _QuickActionBtn(
                icon: '🔍',
                text: 'Check Updates',
                onTap: () {},
              ),
              _QuickActionBtn(
                icon: '⚙️',
                text: 'Settings',
                onTap: () => context.read<AppProvider>().navigateTo(3),
              ),
              _QuickActionBtn(
                icon: '❓',
                text: 'Help',
                onTap: () {},
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildActivityFeed() {
    final activities = [
      ('Cyberpunk 2077', 'Played for 2h', '2 hours ago'),
      ('Elden Ring', 'Achievement unlocked', '5 hours ago'),
      ('Steam Deck', 'Game installed', '1 day ago'),
      ('The Witcher 3', 'Update downloaded', '2 days ago'),
      ('Red Dead Redemption 2', 'Played for 4h', '3 days ago'),
    ];

    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            'Recent Activity',
            style: TextStyle(
              color: AppTheme.textPrimary,
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 15),
          ...activities.map((activity) => _ActivityItem(
            gameName: activity.$1,
            activityType: activity.$2,
            timeAgo: activity.$3,
          )),
        ],
      ),
    );
  }
}

/// Statistic Card Widget
class _StatCard extends StatelessWidget {
  final String title;
  final String value;
  final String icon;
  final Color color;

  const _StatCard({
    required this.title,
    required this.value,
    required this.icon,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(12),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.2),
            blurRadius: 15,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            icon,
            style: const TextStyle(fontSize: 24),
          ),
          const SizedBox(height: 8),
          Text(
            value,
            style: TextStyle(
              color: color,
              fontSize: 32,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            title,
            style: TextStyle(
              color: AppTheme.textSecondary,
              fontSize: 14,
            ),
          ),
        ],
      ),
    );
  }
}

/// Quick Action Button Widget
class _QuickActionBtn extends StatefulWidget {
  final String icon;
  final String text;
  final VoidCallback onTap;

  const _QuickActionBtn({
    required this.icon,
    required this.text,
    required this.onTap,
  });

  @override
  State<_QuickActionBtn> createState() => _QuickActionBtnState();
}

class _QuickActionBtnState extends State<_QuickActionBtn> {
  bool _isHovered = false;

  @override
  Widget build(BuildContext context) {
    return MouseRegion(
      onEnter: (_) => setState(() => _isHovered = true),
      onExit: (_) => setState(() => _isHovered = false),
      child: GestureDetector(
        onTap: widget.onTap,
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 200),
          width: 120,
          height: 120,
          decoration: BoxDecoration(
            color: _isHovered ? AppTheme.surfaceLight : AppTheme.surface,
            border: Border.all(
              color: _isHovered ? AppTheme.primary : AppTheme.surfaceLight,
              width: 2,
            ),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                widget.icon,
                style: const TextStyle(fontSize: 28),
              ),
              const SizedBox(height: 8),
              Text(
                widget.text,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: AppTheme.textPrimary,
                  fontSize: 13,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

/// Activity Item Widget
class _ActivityItem extends StatelessWidget {
  final String gameName;
  final String activityType;
  final String timeAgo;

  const _ActivityItem({
    required this.gameName,
    required this.activityType,
    required this.timeAgo,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 10),
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(8),
        border: Border(
          left: BorderSide(
            color: AppTheme.primary,
            width: 3,
          ),
        ),
      ),
      child: Row(
        children: [
          const Text(
            '🎮',
            style: TextStyle(fontSize: 20),
          ),
          const SizedBox(width: 15),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  gameName,
                  style: const TextStyle(
                    color: AppTheme.textPrimary,
                    fontWeight: FontWeight.w600,
                    fontSize: 14,
                  ),
                ),
                const SizedBox(height: 3),
                Text(
                  '$activityType • $timeAgo',
                  style: TextStyle(
                    color: AppTheme.textSecondary,
                    fontSize: 12,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
