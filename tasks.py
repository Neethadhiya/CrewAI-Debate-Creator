from crewai import Task
from agents import gandhi, hitler

task1 = Task(
    description=(
        'Mahatma Gandhi should present his arguments on the topic: "{debate_topic}" based on his principles of non-violence and peace. '
        'Focus on Gandhi\'s perspective, providing a thorough explanation of his viewpoints and rationale.'
    ),
    agent=gandhi,  # Mahatma Gandhi will handle this task
    async_execution=False,  # Ensure synchronous execution for accurate debate
    expected_output='A comprehensive argument from Mahatma Gandhi on "{debate_topic}", highlighting his principles of non-violence and peace.',
    output_file='argument.md' 
)


task2 = Task(
    description=(
        'Adolf Hitler should present his arguments on the topic: "{debate_topic}" based on his ideology and policies. '
        'Focus on Hitler\'s perspective, providing a thorough explanation of his viewpoints and rationale.'
    ),
    agent=hitler,  # Adolf Hitler will handle this task
    async_execution=False,  # Ensure synchronous execution for accurate debate
    expected_output='A comprehensive argument from Adolf Hitler on "{debate_topic}", highlighting his ideology and policies.',
    output_file='argument.md'  
)

