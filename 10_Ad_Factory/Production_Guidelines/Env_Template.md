# Second Chair Environment Variables

Create a `.env` file in this directory with:

```
# Airtable Personal Access Token for Second Chair base
AIRTABLE_PAT=your_personal_access_token

# Airtable Base ID (found in base URL: airtable.com/BASE_ID/...)
AIRTABLE_BASE_ID=your_base_id
```

## Getting Your Airtable Credentials

1. **Personal Access Token:**
   - Go to https://airtable.com/create/tokens
   - Create a new token with these scopes:
     - `data.records:read`
     - `data.records:write`
     - `schema.bases:write` (required for adding video fields)
   - Add access to your Second Chair base

2. **Base ID:**
   - Open your Second Chair base in Airtable
   - Copy the ID from the URL: `airtable.com/appXXXXXXXXXXXXXX/...`
   - The Base ID starts with `app`
