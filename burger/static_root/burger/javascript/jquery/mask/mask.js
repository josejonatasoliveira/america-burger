$("#id_phone_number").mask('(99) 9 9999-999');

$('#id_email').mask("A", {
    translation: {
        "A": { pattern: /[\w@\-.+]/, recursive: true }
    }
});

$('#id_birthday').mask('99/99/9999');