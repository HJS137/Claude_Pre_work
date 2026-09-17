# Claude 101 

## Lesson 1 - What is claude?
### Objectives
In this Lesson:
 - Explain what claude is and the principles that guide its design.
 - Describe Claudes core capabilities and how it differs from a simple chat bot.
- Identify the different ways to access Claude (web, desktop and mobile)


### Requests
People new to claude often type into it the way they would type into a search box. Here are three real requests. For each one, lets decide could a search box handle it or do we need claude working through it with us. 

1. "Whats the exchange rate from US dollar/ euros today?"
`Search Box `
2. "Rewrite my update below so the delay reads as a decision, not an apology"
`Claude`
3. "best structure for a quaterly business review presentation.
`Claude`


### Ways to access Claude
- Claude.ai
Mobile and desktop apps
- Claude code
Agentic coding tool that is designed for developers but can be used for all kinds of file manipulation on your desktop. 
- Claude Tag
Brings claude into slack 
- Claude Design
Tuning ideas into working interfaces
- Claude for Microsoft 365
Excel, Powerpoint, Word, Outlook

## Lesson 2 - First Convo with Claude
### Writing Effective Prompts
All interactions with claude begin with a prompt, and these prompts, combiend with other context, impact claudes response. Speak to Claude like you would a coworker, naturally, concisely and conversationally. 
1. Setting the stage - what is your role and what are your objectives? Is there a context about your work that Claude should know about?
2. Defining a task: What action do you want Claude to take? Do you want Claude to write analyze, build or something else.
3. Specifying rules: Whats the style or tone you want Claude to use? Are there examples that you can attach to show Claude what your looking for ?


Example of a prompt that uses all three elements:
`I'm the marketing lead at an indie streaming startup, and we're preparing an investor pitch deck for Series A investors. Can you research the current state of the independent film streaming market and identify key trends, competitor positioning, and growth opportunities? Use current web research with citations and structure it as a professional report of up to 5 pages, with an executive summary, market analysis, competitive landscape, and growth opportunities.`

### Adding Context
Uploads, connectors and custom preferences offer ways to give Claude even more context about your work.
Claude can analyze both text and visual elements (like images, charts and graphics) in PDFs and other documents. Supported file types include PDF, DOCX, CSV, TXT and common image formats like PNG and JPEG.

### Iterating on Claudes responses
Guide the conversation based on claudes replies.
- Follow-up questions
- Provide feedback
- Redirect or restart


### Skills

Skills are reusable sets of instructions that teach claude how to approach specific tasks and workflows. They can encode your preferences for everything from how you write and output formats you want to specific processes you follow. This will be continued in lesson 7. 


## Lesson 3 - Getting better results 
### Objectives 
- Recognize common challenges when starting out with AI and use troubleshooting techniques to overcome them.
- Define AI Fluency and know where to go to learn more about working with AI in a fluent way
- Explain how you might set up evals to better understand how claude might perform with your unique workflows


### Common Challenges 

Challenge: Response to generic 
Whats happening: Not enough context
Try: Add more detail about your role, audience, contraints.


Challenge: Response is too long.
Whats happening: Claude is just wrongly guessing the length.
Try this: Be more explicit about the length.

Challenge: Claude didnt follow my format.
Whats happening: Claude understood you but not the way you want it presented.
Try this: Show, dont just tell.


### The Iteration Mindset

Your first prompt rarely produces a perfect result. Therefore you need to give specific feedback and know when to start fresh from a conversation.

### What is AI Fluency?
AI fluency is the ability to collaborate effectively with AI tools - not just knowing which buttons to click.

4d framework for fluency: 
- Delegation: Deciding on what work should be done by humans, what work should be done by AI and how to ditribute tasks between them.
- Description: Effective communication with AI systems. Discussed before.
- Discernment: Thoughtfully and criticallyu evaluating AI outputs, processes, behaviours and interactions. Includes assesing quality, accuracy, appropriateness and determining areas for improvement.
- Dilligence: Using AI responsibly and ethically.


### Why Evals matter?

Work is unique. Running a eval helps you understand where claude adds the most value in your workflow and identify tasks where youll need to provide more context or examples.
Build confidence in claude outputs for recurring tasks.

**A Simple Eval Approach**
You dont need complex infrastructure to evaluate Claude. Heres a pratical approach:

**Gather examples**. Collect 5-10 examples of a task you do regularly—emails you've written, reports you've created, analyses you've done.

**Create test prompts**. Write prompts that would generate similar outputs. Include the context you'd naturally have when doing this work.

**Compare outputs**. Run your prompts and compare Claude's responses to your examples. Ask yourself:
Does Claude capture the key information?
Is the tone and style appropriate?
What's missing or could be improved?

**Refine your approach**. Based on what you learn, adjust your prompts, add examples to show Claude what good looks like, or identify where human review is essential.

## Lesson 4 - Working with Claude on Desktop


### Working with Claude turn by turn

This is claude as a thinking partner: the shape of work where the value is int he exchange itself. You bring a half-formed idea, an unfamiliar dashboard, a paragraph that isnt landing - and you work it out together, one turn at a time.


### Handing of work to Claude 

Working agentically with claude is a new way of working for many people. Instead of asking a question you hand claude a whole piece of work. Gather the context, do the analysis, produce the finished thing - and it comes back done.

**Use this when**: The task has several steps youd normally do in sequence. Pull the figures, compare them, draft the summary, format the doc.
The output is the real deliverable. Word doc or spreadsheet.
The work spans your tools. Rounds up all things at once.

It should happen on schedule.


### Building Software with Claude Code

Desktop app gives you full development environment. Claude works directly in the codebase - reading whats there, writing and modyfying code, running commands. Visual diffs show what changed, a built-in terminal shows commands as they run, git tracks every version so you can always roll back. 

Claude code can work locally, git or cloud.

## Lesson 5 - Introduction to Projects

### Objectives

- Explain what projects are and when to use them 
- Create a new project with a name, description, and visability stage
- Add documents and files to the projects knowledge base
- Write effective project instructions to guide claudes behaviour 
- Share projects with teamates 



### What are Projects?

- Reference mterials used repeatdely
- Consistent requirements for how claude should respond.
- Team collaboration.

- ou need to add project instructions and build a Knowledge base. Projects automatically scale to handle large amounts of data through a process called Retrieval augmented generation (RAG).

## Lesson 6 - Artifacts

### What are Artifacts ?

Artifacts are standalone, interactive outputs that claude creates ina  dedicated window alongside your conversation. This is so long lines of coe dont take uup the project window.

## Lesson 7 - Working with skills


### What are skills?

Folders of instructions, scipts and resources that claude loads dynamically to improve performance on specialised tasks. Think of them as exoertise packages - they teach claude how to complete specific tasks in a repeatable way.

### Types of Skills

- **Anthropic Skills** are created and maintained by Anthropic. These include enhanced document creation capabilities for Excel, Word, PowerPoint, and PDF files. Claude invokes them automatically when relevant, so you don't need to do anything special to use them.
- **Custom skills** are ones you or your organisation create for specialised workflows and domain-specific tasks. For example, you might create a skill that applies your company's brand guidelines to presentations, structures meeting notes in a specific format, or executes your organization's data analysis workflows.

### Enabling Skills

Skills are available on all plans. To use Skills, you'll need to have Code execution and file creation enabled, since Skills require Claude's secure sandboxed computing environment to function. Settings -> cabailities -> skills -> tggle certain skills.


### Security Considerations 

Skills can include executable code, its important to use them thoughtfully:
 - Only install custom skills from trusted sources
 - Anthropics build-in skills are tested and maintained by anthropic

 ### Creating Custom Skills


While Anthropic's built-in Skills cover common document creation tasks, the real power of Skills comes from creating your own. Custom Skills let you teach Claude your specific workflows, brand guidelines, and ways of working—so Claude can apply that knowledge automatically whenever it's relevant.

The easiest way to create a custom Skill is through conversation with Claude itself. You don't need to write code or manually create files—Claude handles the technical structure for you.

Here's how to create a Skill through conversation:

- **Start a new chat** and tell Claude what you want to create. For example: "I want to create a skill for writing quarterly business reviews" or "I need a skill that applies our brand guidelines to presentations."
- **Answer Claude's questions.** Claude will interview you about your workflow, asking things like: What should this skill do? What makes good output for this type of work? Can you give examples of when you'd use this skill?
- **Upload Reference Materials** - Templates, style guides, brand assets.
-  **Save your skill.** When finished, Claude generates a file containing your properly structured skill. All you have to do is save it and the skill will be ready for Claude to use.

## Lesson 8 - Connecting Tools

### What are Connectors?
- **Connectors transform Claude from an assistant into an informed collaborator** by giving Claude access to the same tools, data, and context that you use every day. Instead of starting every conversation from scratch, Claude can work directly with your actual information.
- **Connectors allow Claude to read information and perform actions on your behalf.** Depending on the connector and permissions you grant, Claude can search your files, retrieve documents, analyze data, create new content, update records, and execute tasks across your connected applications—all from within your conversation.
- **The Model Context Protocol (MCP) powers connectors.** Think of MCP like USB-C for AI—a universal standard that allows Claude to connect to many different applications through a single, consistent interface. This open standard means developers can build connectors for any tool, and those connectors work seamlessly with Claude.


### Security and Permissions 

When you connect Claude to external services, you're granting it access to read—and sometimes modify—data within those services. Here are some important considerations:
- **Scoped access:** Permissions are specific to what the connector needs and you can toggle individual permissions on and off within each application's menu.
- **Claude sees what you see:** Claude can only access data you have access to. Connecting your work email doesn't give Claude access to your CEO's inbox—only your own.


## Lesson 9 - Enterprise
*Used for team and enterprise plans*

### What is it ?

Enterprise Search adds a dedicated "Ask {Your Org Name}" option to your sidebar. This is designed specifically for finding and synthesizing knowledge buried across your company's tools and data sources. Think of Enterprise Search as a pre-built project for your entire organization — your company's knowledge base is already loaded, so you can jump right in to get context-aware responses to your questions


### What can you ask?

-*"what happened whilst i was out?"*

-*"How do I submit and expense report?"*

-*"Summarise discussions about the q4 product roadmap"*


## Lesson 10 - Research for deep dives

### What is Research?
Research is an advanced feature that transforms Claude from a conversational assistant into a systematic investigator. When you enable Research, Claude doesn't just answer your question—it explores it from multiple angles, synthesizing information from across the web and your connected integrations.

Think of it as having a skilled research assistant who gathers information, cross-references sources, and compiles a comprehensive report while you stay on your own work.

Research is particularly valuable when you need more than a quick answer. It's designed for situations where a thorough understanding requires pulling together information from multiple sources, comparing different perspectives, and synthesizing findings into actionable insight

### When to use it ?
Use it when you need:
- Comprehensive reports that synthesize information from multiple sources.
- Thorough investigations that would typically require hours of manual work.
- Report with citations you can verify.

-- end ---

