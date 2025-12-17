class UserEntity {
  final String id;
  final String name;
  final String email;
  final UserRole role;
  final DateTime createdAt;

  const UserEntity({
    required this.id,
    required this.name,
    required this.email,
    this.role = UserRole.user,
    required this.createdAt,
  });
}

enum UserRole {
  user,
  admin,
}
