class ImageEntity {
  final String id;
  final String url;
  final ImageType type;

  const ImageEntity({
    required this.id,
    required this.url,
    this.type = ImageType.gallery,
  });
}
