class FavoriteEntity {
  final String userId;
  final int pointTourismId;
  final DateTime savedAt;

  const FavoriteEntity({
    required this.userId,
    required this.pointTourismId,
    required this.savedAt,
  });
}
