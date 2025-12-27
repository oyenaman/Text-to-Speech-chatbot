import asyncio
import edge_tts

async def list_english_voices():
    """List only English voices with neural ones first"""
    voices = await edge_tts.list_voices()
    
    print("=" * 80)
    print("ENGLISH VOICES FOR AWARD ANNOUNCEMENTS")
    print("=" * 80)
    
    english_voices = [v for v in voices if v['Locale'].startswith('en')]
    
    neural_voices = [v for v in english_voices if 'Neural' in v['ShortName']]
    standard_voices = [v for v in english_voices if 'Neural' not in v['ShortName']]
    
    print("\n🎙️  NEURAL VOICES (Recommended - High Quality)")
    print("-" * 50)
    for voice in sorted(neural_voices, key=lambda x: x['ShortName']):
        print(f"{voice['ShortName']:25} | {voice['FriendlyName']:35} | {voice['Gender']:6} | {voice['Locale']}")
    
    print("\n🔊 STANDARD VOICES")
    print("-" * 50)
    for voice in sorted(standard_voices, key=lambda x: x['ShortName']):
        print(f"{voice['ShortName']:25} | {voice['FriendlyName']:35} | {voice['Gender']:6} | {voice['Locale']}")

asyncio.run(list_english_voices())