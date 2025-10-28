# Feature idea: create custom prompts with voice!

**Posted:** 2025-05-27 17:11:09
**Author:** u/danielrosehill
**Subreddit:** r/Voicenotesai
**URL:** https://www.reddit.com/r/Voicenotesai/comments/1kwo9l7/feature_idea_create_custom_prompts_with_voice/
**Score:** 5 upvotes
**Comments:** 5

---

## Content

So ... my last post demonstrated that custom prompts can yield sucky results. So here's me back writing in my regular tone of voice!

Here's a strategy that I've used successfully: using an AI "agent" (etc) to create what I call text transformation prompts: the "custom prompts" that convert the dictated text into specific formats.

Workflow is basically this:

I dictate my idea for a text transformation prompt. As usual, it gets transcribed in a way that's accurate but not optimal.

Then, that gets sent to the .... text transformation writing agent which has a system promptlike this:

*Take the text provided by the user and reformat it into a custom prompt to be used by an AI writing assistant for the purpose of transforming text from a raw transcription into a formatted version intended for a specific use case.* 

Prompt with an example (usually significantly improves performance in my experience):

*Take the text provided by the user and reformat it into a custom prompt to be used by an AI writing assistant for the purpose of transforming text from a raw transcription into a formatted version intended for a specific use case. Here's an example of a prompt which you can use as a model: 'take the text provided by the user and reformat it into a polished business-appropriate email. Ensure paragraph spacing, the use of business-appropriate language, and maintain a friendly but professional tone of voice.'*

UI implementation:

Create a prompt with your voice!

User records voice note -> sends to AI with above system prompt -> finished prompt is returned to the user or (better) added to the user's custom prompt library with a good name. 

---

## Metadata

- **Post ID:** 1kwo9l7
- **Permalink:** https://reddit.com/r/Voicenotesai/comments/1kwo9l7/feature_idea_create_custom_prompts_with_voice/
- **Flair:** None
