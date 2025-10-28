# Improved system prompts for note reformatting (request, idea)

**Posted:** 2025-05-21 19:46:12
**Author:** u/danielrosehill
**Subreddit:** r/Voicenotesai
**URL:** https://www.reddit.com/r/Voicenotesai/comments/1ks2ngr/improved_system_prompts_for_note_reformatting/
**Score:** 5 upvotes
**Comments:** 3

---

## Content

Hello Voicenotes team,

Sorry to flood your subreddit!

Perhaps you guys might consider adding a feature request tracker so that engaged users can add these without feeling like we're monopolising spaces like this.

In any event, I felt that this was one worth getting across to you. Unfortunately, I only have personal business emails in my voice note history, which would be a lot of work to redact, so instead I'll just describe it.

When I create a note and choose email as the target format, it renders as a continuous block of text, Much like the input. As far as I know, this is consistent across the formatting types.

I've had success in mitigating this behavior with some simple edits to system prompts. Rather than share those in full, I'll just explain what I added.

Something like:

"... Take the text provided by the user and add paragraph spacing where appropriate."

To improve adherence, you can add an example. And integrating it into a email writing system prompt would be something like:

" Take the text provided by the user and reformat it o adhere to the standard formatting of an email, Ensuring that you add spacing between paragraphs. "

The problem without the paragraph spacing Is that it returns the text as a continuous block so I have to then manually add the spacing in before sending. 

Hope this helps! 

---

## Metadata

- **Post ID:** 1ks2ngr
- **Permalink:** https://reddit.com/r/Voicenotesai/comments/1ks2ngr/improved_system_prompts_for_note_reformatting/
- **Flair:** Discussion
