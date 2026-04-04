Instructions:
Please use this template when a structured explanation is asked for. Carefully adhere to the following specifications for each section. The sections to be included are (1) system context, (2) step-by-step explanation requested (3) links to relevant information, (4) mechanistic clarifications, (5) a resource tree showing the key resources under discussion, (6) a call tree or control-flow graph showing 

Details regarding the sections:

1. System context succinctly describes the "funnel" from the project down to the sub-system being discussed. 
2. Step-by-step explanation is a detailed, linear flow describing how something works.
3. Links to files and line numbers the user can inspect to verify 1 and 2.
4. The mechanistic clarifications list is a set of details required for understanding items in (2).
5. Resource tree describing the locations of items under discussion. Use plain text with indentation for hierarchy in a code format block.
6. Call-tree or control-flow graph describing how the system described in the step-by-step walkthrough and resources tree actually works.

Omit 4 as necessary.

Follow the template below:

[One sentance topic statement]

System context:
- [Description of outermost layer of project this system belongs to. 10 words or less, no formatting]
- [Description of next semantically important sub-system the topic system is under. 10 words or less, no formatting]
- [Repeat as necessary for additional important layers. 10 words or less, no formatting]
- [Description of the sub-system you will unpack step-wise. 10 words or less, no formatting]

Step-by-step walkthrough:
- [Description of purpose of sub-system the user asked about. 10 words or less, no formatting]
- [Description of sub-system entry point, same rules]
- [Descriptions, one concept per line, of how the system proceeds, same rules, repeat as necessary]

Links:
- [Sub-system name: [link text], repeat as needed]
[...]

Mechanistism clarifications:
- [Describe or define any non-standard or codebase specific concepts referend in 1 or 2. 10 words or less, no formatting]
- [Repeat as necessary, same rules.]

Diagram:
```
example_package/
   example_module.py
      example_function()
   second_example_module.py
      example_class()
```
Consider using the resource tree skill to help generate information going into the explanation.