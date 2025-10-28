#!/usr/bin/env python3
"""
Fetch Reddit posts and save them as markdown files.
Uses Reddit API credentials to fetch post content.
"""

import praw
import os
from datetime import datetime
import re

# Reddit API credentials
CLIENT_ID = "2YgS27cy2xGXSLzxiJPiBw"
CLIENT_SECRET = "wqfKdfRXr_L8XvpIPkMmaGk0_egvBQ"
USER_AGENT = "python:feature-requests-fetcher:v1.0 (by /u/danielrosehill)"

# Voicenotes post URLs
VOICENOTES_URLS = [
    "https://www.reddit.com/r/Voicenotesai/comments/1n1m0z1/voicenotes_todoist_smart_date_recognition/",
    "https://www.reddit.com/r/Voicenotesai/comments/1mtjfhv/feature_idea_fix_word_add_to_dictionary/",
    "https://www.reddit.com/r/Voicenotesai/comments/1mlxsup/feature_request_highlight_for_webhooklinked_tags/",
    "https://www.reddit.com/r/Voicenotesai/comments/1mdyjzs/feature_request_hierarchical_tags_taxonomy_and/",
    "https://www.reddit.com/r/Voicenotesai/comments/1mdygv6/feature_request_multiaccount_support/",
    "https://www.reddit.com/r/Voicenotesai/comments/1mc82p1/fr_the_ability_to_name_webhooks/",
    "https://www.reddit.com/r/Voicenotesai/comments/1m5gh0m/fr_accidental_recording_detection_and_prevention/",
    "https://www.reddit.com/r/Voicenotesai/comments/1m4n2m8/feature_idea_tag_to_prompt_automations/",
    "https://www.reddit.com/r/Voicenotesai/comments/1lwchmm/feature_request_note_backup_export/",
    "https://www.reddit.com/r/Voicenotesai/comments/1kwo9l7/feature_idea_create_custom_prompts_with_voice/",
    "https://www.reddit.com/r/Voicenotesai/comments/1kwo4y9/feature_idea_user_personalisation_elements_name/",
    "https://www.reddit.com/r/Voicenotesai/comments/1ktjaqr/feature_request_verbatimunedited_output_option/",
    "https://www.reddit.com/r/Voicenotesai/comments/1ks2ngr/improved_system_prompts_for_note_reformatting/",
    "https://www.reddit.com/r/Voicenotesai/comments/1kqcct6/fr_bluetooth_microphone_source_for_android/",
    "https://www.reddit.com/r/Voicenotesai/comments/1kpi8uk/feature_request_configurable_webhook_integration/",
    "https://www.reddit.com/r/Voicenotesai/comments/1kpi6p4/feature_request_more_keyboard_shortcuts/",
]

def sanitize_filename(title):
    """Convert title to a valid filename."""
    # Remove or replace invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '', title)
    # Replace spaces with hyphens
    filename = filename.replace(' ', '-')
    # Limit length
    filename = filename[:100]
    # Remove trailing hyphens or dots
    filename = filename.rstrip('-.')
    return filename.lower()

def fetch_and_save_posts():
    """Fetch Reddit posts and save them as markdown files."""

    # Initialize Reddit instance
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )

    # Create voicenotes directory if it doesn't exist
    output_dir = "voicenotes"
    os.makedirs(output_dir, exist_ok=True)

    print(f"Fetching {len(VOICENOTES_URLS)} Voicenotes feature requests...\n")

    successful = 0
    failed = 0

    for url in VOICENOTES_URLS:
        try:
            # Extract submission ID from URL
            submission = reddit.submission(url=url)

            # Generate filename from title
            filename = sanitize_filename(submission.title)
            filepath = os.path.join(output_dir, f"{filename}.md")

            # Create markdown content
            content = f"""# {submission.title}

**Posted:** {datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')}
**Author:** u/{submission.author.name if submission.author else '[deleted]'}
**Subreddit:** r/{submission.subreddit.display_name}
**URL:** {submission.url}
**Score:** {submission.score} upvotes
**Comments:** {submission.num_comments}

---

## Content

{submission.selftext}

---

## Metadata

- **Post ID:** {submission.id}
- **Permalink:** https://reddit.com{submission.permalink}
- **Flair:** {submission.link_flair_text if submission.link_flair_text else 'None'}
"""

            # Save to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"✓ Saved: {filename}.md")
            successful += 1

        except Exception as e:
            print(f"✗ Failed to fetch {url}: {str(e)}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"Summary: {successful} successful, {failed} failed")
    print(f"Files saved to: {os.path.abspath(output_dir)}/")

if __name__ == "__main__":
    fetch_and_save_posts()
