import 'package:flutter/foundation.dart';

/// Game model
class Game {
  final String id;
  final String name;
  final String? path;
  final double size;
  final DateTime? installDate;
  final DateTime? lastPlayed;
  final int playTime; // in minutes
  final String status; // 'Installed', 'Not Installed', 'Updating', etc.
  final String? genre;
  final double? rating;
  final String? coverUrl;
  final bool isFavorite;

  Game({
    required this.id,
    required this.name,
    this.path,
    this.size = 0,
    this.installDate,
    this.lastPlayed,
    this.playTime = 0,
    this.status = 'Not Installed',
    this.genre,
    this.rating,
    this.coverUrl,
    this.isFavorite = false,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'name': name,
      'path': path,
      'size': size,
      'install_date': installDate?.toIso8601String(),
      'last_played': lastPlayed?.toIso8601String(),
      'play_time': playTime,
      'status': status,
      'genre': genre,
      'rating': rating,
      'cover_url': coverUrl,
      'is_favorite': isFavorite ? 1 : 0,
    };
  }

  factory Game.fromMap(Map<String, dynamic> map) {
    return Game(
      id: map['id']?.toString() ?? '',
      name: map['name'] ?? 'Unknown Game',
      path: map['path'],
      size: (map['size'] ?? 0).toDouble(),
      installDate: map['install_date'] != null 
          ? DateTime.tryParse(map['install_date']) 
          : null,
      lastPlayed: map['last_played'] != null 
          ? DateTime.tryParse(map['last_played']) 
          : null,
      playTime: map['play_time'] ?? 0,
      status: map['status'] ?? 'Not Installed',
      genre: map['genre'],
      rating: map['rating'] != null 
          ? (map['rating'] as num).toDouble() 
          : null,
      coverUrl: map['cover_url'],
      isFavorite: map['is_favorite'] == 1 || map['is_favorite'] == true,
    );
  }

  Game copyWith({
    String? id,
    String? name,
    String? path,
    double? size,
    DateTime? installDate,
    DateTime? lastPlayed,
    int? playTime,
    String? status,
    String? genre,
    double? rating,
    String? coverUrl,
    bool? isFavorite,
  }) {
    return Game(
      id: id ?? this.id,
      name: name ?? this.name,
      path: path ?? this.path,
      size: size ?? this.size,
      installDate: installDate ?? this.installDate,
      lastPlayed: lastPlayed ?? this.lastPlayed,
      playTime: playTime ?? this.playTime,
      status: status ?? this.status,
      genre: genre ?? this.genre,
      rating: rating ?? this.rating,
      coverUrl: coverUrl ?? this.coverUrl,
      isFavorite: isFavorite ?? this.isFavorite,
    );
  }
}
