class AlbumEntity {
  final String id;
  final String title;
  final List<ImageEntity> images;

  const AlbumEntity({
    required this.id,
    required this.title,
    required this.images,
  });
}
