import funcs
import assignment_operators
import identity_operators
import membership_operators
import ternary_operators


while True:
    funcs.clear_screen()
    funcs.about_program()

    # build topics directory
    main_topics = {
        '1': 'Operators'
        }

    operator_topics = {
        '1': 'Assignment Operators',
        '2': 'Identity Operators',
        '3': 'Membership Operators',
        '4': 'Ternary Operators'
    }

    while True:
        selected_topic = funcs.topic_selection(main_topics)

        try:
            if selected_topic is None:
                raise ValueError
        except ValueError:
            funcs.invalid_selection()
            continue
        else:
            break

    funcs.clear_screen()

    if selected_topic == 'Operators':
        funcs.your_selected_topic_is(selected_topic)

        while True:
            selected_topic = funcs.topic_selection(operator_topics)

            try:
                if selected_topic is None:
                    raise ValueError
            except ValueError:
                funcs.invalid_selection()
                continue
            else:
                break

    funcs.clear_screen()
    answer = False

    while answer is not True:
        if selected_topic == 'Assignment Operators':
            assignment_operators.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Identity Operators':
            identity_operators.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Membership Operators':
            membership_operators.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Ternary Operators':
            ternary_operators.intro()
            while answer is not True:
                answer = funcs.goback()
