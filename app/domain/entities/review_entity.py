class ReviewEntity {
  final String id;
  final String userId;
  final int pointTourismId;
  final double rating; // 1.0 a 5.0
  final String? comment;
  final DateTime createdAt;

  const ReviewEntity({
    required this.id,
    required this.userId,
    required this.pointTourismId,
    required this.rating,
    this.comment,
    required this.createdAt,
  });
}
