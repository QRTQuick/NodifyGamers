import 'package:flutter/material.dart';
import '../utils/theme.dart';

/// News & Updates screen with categorized feeds
class NewsScreen extends StatelessWidget {
  const NewsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(30),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header
            _buildHeader(),
            const SizedBox(height: 20),
            
            // Tab bar
            _buildTabBar(),
            const SizedBox(height: 20),
            
            // Tab content
            SizedBox(
              height: 600,
              child: TabBarView(
                children: [
                  _buildNewsTab(),
                  _buildUpdatesTab(),
                  _buildEventsTab(),
                ],
              ),
            ),
          ],
        ),
      ),
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
              'News & Updates',
              style: TextStyle(
                color: AppTheme.textPrimary,
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          ElevatedButton.icon(
            onPressed: () {},
            icon: const Icon(Icons.refresh),
            label: const Text('Refresh'),
            style: ElevatedButton.styleFrom(
              backgroundColor: AppTheme.primary,
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTabBar() {
    return Container(
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(12),
      ),
      child: const TabBar(
        labelColor: AppTheme.textPrimary,
        unselectedLabelColor: AppTheme.textSecondary,
        indicatorColor: AppTheme.primary,
        indicatorSize: TabBarIndicatorSize.tab,
        padding: EdgeInsets.all(8),
        tabs: [
          Tab(text: '📰 Latest News', height: 50),
          Tab(text: '🔄 Game Updates', height: 50),
          Tab(text: '🎉 Events', height: 50),
        ],
      ),
    );
  }

  Widget _buildNewsTab() {
    final newsItems = [
      {
        'title': 'Major Platform Update Released',
        'excerpt': 'Discover the new features and improvements in our latest platform update including performance boosts and UI enhancements.',
        'date': 'Today',
        'category': 'Platform',
      },
      {
        'title': 'Summer Sale Event Starting Soon',
        'excerpt': 'Get ready for massive discounts on hundreds of games. The summer sale starts next week with deals up to 80% off.',
        'date': 'Yesterday',
        'category': 'Events',
      },
      {
        'title': 'New Achievement System Launched',
        'excerpt': 'Track your gaming accomplishments with our revamped achievement system featuring global leaderboards.',
        'date': '2 days ago',
        'category': 'Features',
      },
    ];

    return ListView.separated(
      itemCount: newsItems.length,
      separatorBuilder: (_, __) => const SizedBox(height: 15),
      itemBuilder: (context, index) {
        return _NewsCard(news: newsItems[index]);
      },
    );
  }

  Widget _buildUpdatesTab() {
    final updates = [
      ('Cyberpunk 2077', '2.1', '45 GB', 'Today'),
      ('Elden Ring', '1.10', '12 GB', 'Yesterday'),
      ('The Witcher 3', '4.04', '8 GB', '3 days ago'),
      ('Red Dead Redemption 2', '1.28', '15 GB', '1 week ago'),
    ];

    return ListView.separated(
      itemCount: updates.length,
      separatorBuilder: (_, __) => const SizedBox(height: 10),
      itemBuilder: (context, index) {
        return _UpdateItem(
          gameName: updates[index].$1,
          version: updates[index].$2,
          size: updates[index].$3,
          date: updates[index].$4,
        );
      },
    );
  }

  Widget _buildEventsTab() {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text(
            '🎉',
            style: TextStyle(fontSize: 60),
          ),
          const SizedBox(height: 20),
          Text(
            'Upcoming Events',
            style: TextStyle(
              color: AppTheme.textPrimary,
              fontSize: 20,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 10),
          Text(
            'No events scheduled at the moment.\nCheck back soon for exciting gaming events!',
            textAlign: TextAlign.center,
            style: TextStyle(
              color: AppTheme.textSecondary,
              fontSize: 16,
            ),
          ),
        ],
      ),
    );
  }
}

/// News Card Widget
class _NewsCard extends StatelessWidget {
  final Map<String, String> news;

  const _NewsCard({required this.news});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 180,
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
      child: Row(
        children: [
          // Image section
          Container(
            width: 200,
            decoration: const BoxDecoration(
              gradient: AppTheme.primaryGradient,
            ),
            child: const Center(
              child: Text(
                '📰',
                style: TextStyle(fontSize: 48),
              ),
            ),
          ),
          // Content section
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    news['title']!,
                    style: const TextStyle(
                      color: AppTheme.textPrimary,
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 10),
                  Text(
                    news['excerpt']!,
                    style: TextStyle(
                      color: AppTheme.textSecondary,
                      fontSize: 14,
                    ),
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const Spacer(),
                  Row(
                    children: [
                      Text(
                        '📅 ${news['date']}',
                        style: TextStyle(
                          color: AppTheme.textMuted,
                          fontSize: 12,
                        ),
                      ),
                      const SizedBox(width: 15),
                      Text(
                        '🏷️ ${news['category']}',
                        style: const TextStyle(
                          color: AppTheme.primary,
                          fontSize: 12,
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

/// Update Item Widget
class _UpdateItem extends StatelessWidget {
  final String gameName;
  final String version;
  final String size;
  final String date;

  const _UpdateItem({
    required this.gameName,
    required this.version,
    required this.size,
    required this.date,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 90,
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 15),
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(12),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.15),
            blurRadius: 10,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Row(
        children: [
          const Text(
            '⬇️',
            style: TextStyle(fontSize: 32),
          ),
          const SizedBox(width: 20),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  gameName,
                  style: const TextStyle(
                    color: AppTheme.textPrimary,
                    fontWeight: FontWeight.bold,
                    fontSize: 16,
                  ),
                ),
                const SizedBox(height: 5),
                Text(
                  'Version $version • $size • $date',
                  style: TextStyle(
                    color: AppTheme.textSecondary,
                    fontSize: 13,
                  ),
                ),
              ],
            ),
          ),
          ElevatedButton(
            onPressed: () {},
            style: ElevatedButton.styleFrom(
              backgroundColor: AppTheme.primary,
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8),
              ),
            ),
            child: const Text('Update Now'),
          ),
        ],
      ),
    );
  }
}
