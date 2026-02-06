SELECT
  lesson_id,
  weekday,
  start_hour,
  start_minute,
  end_hour,
  end_minute,
  lessons.classroom_id,
  classroom_short_name,
  classroom_display_name AS classroom_name,
  teachers.teacher_initials,
  teacher_name,
  short_subject_name,
  subject_name,
  (
    SELECT
      JSON_ARRAYAGG(student_groups.group_name)
    FROM
      group_lessons
      LEFT JOIN student_groups ON (group_lessons.group_id = student_groups.group_id)
    WHERE
      (lessons.lesson_id = group_lessons.lesson_id)
  ) AS `groups`,
  (
    SELECT
      JSON_ARRAYAGG(
        JSON_OBJECT(
          'subgroup_id',
          subgroup_lessons.subgroup_id,
          'subgroup_name',
          subgroups.subgroup_name,
          'subgroup_display_name',
          subgroups.subgroup_display_name,
          'group_id',
          subgroups.group_id,
          'group_name',
          student_groups.group_name
        )
      ) AS subgroups
    FROM
      subgroup_lessons
      LEFT JOIN subgroups ON (subgroup_lessons.subgroup_id = subgroups.subgroup_id)
      LEFT JOIN student_groups ON (subgroups.group_id = student_groups.group_id)
    WHERE
      (lessons.lesson_id = subgroup_lessons.lesson_id)
  ) AS subgroups
FROM
  lessons
  LEFT JOIN classrooms ON (lessons.classroom_id = classrooms.classroom_id)
  LEFT JOIN teachers ON (lessons.teacher_initials = teachers.teacher_initials)
  LEFT JOIN subjects ON (lessons.short_subject_name = subjects.subject_short_name)
WHERE
  (
    lesson_id IN (
      SELECT
        lesson_id
      FROM
        group_lessons
      WHERE
        (group_id = (SELECT group_id FROM student_groups WHERE group_name = %s)) UNION
      SELECT
        lesson_id
      FROM
        subgroup_lessons
        LEFT JOIN subgroups ON (subgroup_lessons.subgroup_id = subgroups.subgroup_id)
      WHERE
        subgroup_lessons.subgroup_id IN (SELECT subgroup_id FROM subgroups WHERE group_id = (SELECT group_id FROM student_groups WHERE group_name = %s))
    ) AND
    semester_id = 1
  )
ORDER BY
  weekday,
  start_hour ASC;