class Recipe {
  final int id;
  final String title;
  final String ingr;
  final String inst;
  final String level;
  final String time;

  Recipe({
    required this.id,
    required this.title,
    required this.ingr,
    required this.inst,
    required this.level,
    required this.time
  });

  // Add copyWith method
  Recipe copyWith({
    int? id,
    String? title,
    String? ingr,
    String? inst,
    String? level,
    String? time
  }) {
    return Recipe(
      id: id ?? this.id,
      title: title ?? this.title,
      ingr: ingr ?? this.ingr,
      inst: inst ?? this.inst,
      level: level ?? this.level,
      time: time ?? this.time
    );
  }

}
