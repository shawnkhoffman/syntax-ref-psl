import funcs
import datatypes_strings
import datatypes_lists
import datatypes_tuples
import datatypes_iterations
import operators_division
import operators_assignment
import operators_identity
import operators_membership
import operators_ternary
import operator_overloading
import operators_any_all
import operator_functions


while True:
    funcs.clear_screen()
    funcs.about_program()

    # build topics directory
    main_topics = {
        '1': 'Data Types',
        '2': 'Operators',
        }

    datatypes_topics = {
        '1': 'Strings',
        '2': 'Lists',
        '3': 'Tuples',
        '6': 'Iterations'
    }

    operator_topics = {
        '1': 'Assignment Operators',
        '2': 'Identity Operators',
        '3': 'Membership Operators',
        '4': 'Ternary Operators',
        '5': 'Division Operators',
        '6': 'Operator Overloading',
        '7': 'Any/All Operators',
        '8': 'Operator Functions'
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

    elif selected_topic == 'Data Types':
        funcs.your_selected_topic_is(selected_topic)

        while True:
            selected_topic = funcs.topic_selection(datatypes_topics)

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
        if selected_topic == 'Strings':
            datatypes_strings.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Lists':
            datatypes_lists.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Tuples':
            datatypes_tuples.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Iterations':
            datatypes_iterations.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Assignment Operators':
            operators_assignment.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Identity Operators':
            operators_identity.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Membership Operators':
            operators_membership.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Ternary Operators':
            operators_ternary.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Division Operators':
            operators_division.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Operator Overloading':
            operator_overloading.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Any/All Operators':
            operators_any_all.intro()
            while answer is not True:
                answer = funcs.goback()

        if selected_topic == 'Operator Functions':
            operator_functions.intro()
            while answer is not True:
                answer = funcs.goback()
