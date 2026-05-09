import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/games_provider.dart';
import '../utils/theme.dart';

/// Game Library screen with grid/list views, search, and filtering
class GameLibraryScreen extends StatelessWidget {
  const GameLibraryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer<GamesProvider>(
      builder: (context, gamesProvider, child) {
        return SingleChildScrollView(
          padding: const EdgeInsets.all(30),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Header with search
              _buildHeader(gamesProvider),
              const SizedBox(height: 20),
              
              // Toolbar with filters and view toggle
              _buildToolbar(context, gamesProvider),
              const SizedBox(height: 20),
              
              // Games grid or list
              if (gamesProvider.isLoading)
                const Center(child: CircularProgressIndicator())
              else
                gamesProvider.isGridView
                    ? _buildGridView(gamesProvider)
                    : _buildListView(gamesProvider),
            ],
          ),
        );
      },
    );
  }

  Widget _buildHeader(GamesProvider gamesProvider) {
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
              'My Game Library',
              style: TextStyle(
                color: AppTheme.textPrimary,
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          SizedBox(
            width: 300,
            child: TextField(
              onChanged: gamesProvider.setSearchQuery,
              decoration: InputDecoration(
                hintText: '🔍 Search games...',
                prefixIcon: const Icon(Icons.search, color: AppTheme.primary),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildToolbar(BuildContext context, GamesProvider gamesProvider) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 15),
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(12),
      ),
      child: Row(
        children: [
          // Filter dropdown
          Text(
            'Filter:',
            style: TextStyle(color: AppTheme.textSecondary, fontSize: 14),
          ),
          const SizedBox(width: 10),
          Container(
            width: 150,
            decoration: BoxDecoration(
              color: AppTheme.surface,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: AppTheme.surfaceLight),
            ),
            child: DropdownButtonHideUnderline(
              child: DropdownButton<String>(
                value: gamesProvider.filterType,
                isExpanded: true,
                dropdownColor: AppTheme.surface,
                items: ['All Games', 'Installed', 'Not Installed', 'Favorites']
                    .map((type) => DropdownMenuItem(
                          value: type,
                          child: Text(
                            type,
                            style: const TextStyle(color: AppTheme.textPrimary),
                          ),
                        ))
                    .toList(),
                onChanged: (value) {
                  if (value != null) gamesProvider.setFilterType(value);
                },
              ),
            ),
          ),
          const SizedBox(width: 30),
          
          // Sort dropdown
          Text(
            'Sort by:',
            style: TextStyle(color: AppTheme.textSecondary, fontSize: 14),
          ),
          const SizedBox(width: 10),
          Container(
            width: 150,
            decoration: BoxDecoration(
              color: AppTheme.surface,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: AppTheme.surfaceLight),
            ),
            child: DropdownButtonHideUnderline(
              child: DropdownButton<String>(
                value: gamesProvider.sortBy,
                isExpanded: true,
                dropdownColor: AppTheme.surface,
                items: ['Name', 'Last Played', 'Install Date', 'Play Time']
                    .map((type) => DropdownMenuItem(
                          value: type,
                          child: Text(
                            type,
                            style: const TextStyle(color: AppTheme.textPrimary),
                          ),
                        ))
                    .toList(),
                onChanged: (value) {
                  if (value != null) gamesProvider.setSortBy(value);
                },
              ),
            ),
          ),
          const Spacer(),
          
          // View toggle buttons
          _ViewToggleBtn(
            icon: Icons.grid_on,
            label: 'Grid',
            isActive: gamesProvider.isGridView,
            onTap: () {
              if (!gamesProvider.isGridView) gamesProvider.toggleViewMode();
            },
          ),
          const SizedBox(width: 10),
          _ViewToggleBtn(
            icon: Icons.list,
            label: 'List',
            isActive: !gamesProvider.isGridView,
            onTap: () {
              if (gamesProvider.isGridView) gamesProvider.toggleViewMode();
            },
          ),
        ],
      ),
    );
  }

  Widget _buildGridView(GamesProvider gamesProvider) {
    final games = gamesProvider.filteredGames;
    
    if (games.isEmpty) {
      return Center(
        child: Text(
          'No games found',
          style: TextStyle(color: AppTheme.textSecondary, fontSize: 16),
        ),
      );
    }

    return GridView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 4,
        mainAxisSpacing: 20,
        crossAxisSpacing: 20,
        childAspectRatio: 0.72,
      ),
      itemCount: games.length,
      itemBuilder: (context, index) {
        return _GameCard(game: games[index]);
      },
    );
  }

  Widget _buildListView(GamesProvider gamesProvider) {
    final games = gamesProvider.filteredGames;
    
    if (games.isEmpty) {
      return Center(
        child: Text(
          'No games found',
          style: TextStyle(color: AppTheme.textSecondary, fontSize: 16),
        ),
      );
    }

    return ListView.separated(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      itemCount: games.length,
      separatorBuilder: (_, __) => const SizedBox(height: 10),
      itemBuilder: (context, index) {
        return _GameListItem(game: games[index]);
      },
    );
  }
}

/// View Toggle Button
class _ViewToggleBtn extends StatefulWidget {
  final IconData icon;
  final String label;
  final bool isActive;
  final VoidCallback onTap;

  const _ViewToggleBtn({
    required this.icon,
    required this.label,
    required this.isActive,
    required this.onTap,
  });

  @override
  State<_ViewToggleBtn> createState() => _ViewToggleBtnState();
}

class _ViewToggleBtnState extends State<_ViewToggleBtn> {
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
          width: 80,
          height: 40,
          decoration: BoxDecoration(
            color: widget.isActive
                ? AppTheme.primary
                : (_isHovered ? AppTheme.surfaceLight : AppTheme.surface),
            borderRadius: BorderRadius.circular(8),
          ),
          child: Center(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  widget.icon,
                  size: 18,
                  color: widget.isActive
                      ? Colors.white
                      : (_isHovered ? AppTheme.primary : AppTheme.textSecondary),
                ),
                const SizedBox(width: 5),
                Text(
                  widget.label,
                  style: TextStyle(
                    color: widget.isActive
                        ? Colors.white
                        : (_isHovered ? AppTheme.primary : AppTheme.textSecondary),
                    fontSize: 13,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

/// Game Card Widget for Grid View
class _GameCard extends StatefulWidget {
  final dynamic game;

  const _GameCard({required this.game});

  @override
  State<_GameCard> createState() => _GameCardState();
}

class _GameCardState extends State<_GameCard> {
  bool _isHovered = false;

  @override
  Widget build(BuildContext context) {
    return MouseRegion(
      onEnter: (_) => setState(() => _isHovered = true),
      onExit: (_) => setState(() => _isHovered = false),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        decoration: BoxDecoration(
          color: _isHovered ? AppTheme.surfaceLight : AppTheme.surface,
          borderRadius: BorderRadius.circular(8),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.2),
              blurRadius: _isHovered ? 20 : 15,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Cover image placeholder
            Expanded(
              child: Container(
                width: double.infinity,
                decoration: BoxDecoration(
                  gradient: AppTheme.cardGradient,
                  borderRadius: const BorderRadius.vertical(
                    top: Radius.circular(8),
                  ),
                ),
                child: Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Text(
                        '🎮',
                        style: TextStyle(fontSize: 40),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        widget.game.name,
                        textAlign: TextAlign.center,
                        style: const TextStyle(
                          color: AppTheme.textPrimary,
                          fontSize: 14,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
            // Info section
            Container(
              padding: const EdgeInsets.all(12),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    widget.game.name,
                    style: const TextStyle(
                      color: AppTheme.textPrimary,
                      fontWeight: FontWeight.bold,
                      fontSize: 14,
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 5),
                  Row(
                    children: [
                      Container(
                        width: 8,
                        height: 8,
                        decoration: BoxDecoration(
                          color: widget.game.status == 'Installed'
                              ? AppTheme.secondary
                              : AppTheme.textMuted,
                          shape: BoxShape.circle,
                        ),
                      ),
                      const SizedBox(width: 5),
                      Text(
                        widget.game.status,
                        style: TextStyle(
                          color: widget.game.status == 'Installed'
                              ? AppTheme.secondary
                              : AppTheme.textMuted,
                          fontSize: 12,
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

/// Game List Item Widget for List View
class _GameListItem extends StatelessWidget {
  final dynamic game;

  const _GameListItem({required this.game});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(15),
      decoration: BoxDecoration(
        color: AppTheme.surface,
        borderRadius: BorderRadius.circular(8),
      ),
      child: Row(
        children: [
          // Cover thumbnail
          Container(
            width: 60,
            height: 60,
            decoration: BoxDecoration(
              gradient: AppTheme.cardGradient,
              borderRadius: BorderRadius.circular(8),
            ),
            child: const Center(
              child: Text(
                '🎮',
                style: TextStyle(fontSize: 30),
              ),
            ),
          ),
          const SizedBox(width: 15),
          
          // Game info
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  game.name,
                  style: const TextStyle(
                    color: AppTheme.textPrimary,
                    fontWeight: FontWeight.bold,
                    fontSize: 15,
                  ),
                ),
                const SizedBox(height: 5),
                Text(
                  '${game.genre ?? 'N/A'} • Last played: ${game.lastPlayed != null ? _formatDate(game.lastPlayed) : 'Never'}',
                  style: TextStyle(
                    color: AppTheme.textSecondary,
                    fontSize: 13,
                  ),
                ),
              ],
            ),
          ),
          
          // Play button
          ElevatedButton(
            onPressed: () {},
            style: ElevatedButton.styleFrom(
              backgroundColor: AppTheme.secondary,
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8),
              ),
            ),
            child: const Text('▶ Play'),
          ),
        ],
      ),
    );
  }

  String _formatDate(DateTime date) {
    return '${date.day}/${date.month}/${date.year}';
  }
}
