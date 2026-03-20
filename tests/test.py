# import http

# sdk_http_response=HttpResponse(
#   headers=<dict len=11>
# ) candidates=[Candidate(
#   content=Content(
#     parts=[
#       Part(
#         text='Hello! How can I help you today?'
#       ),
#     ],
#     role='model'
#   ),
#   finish_reason=<FinishReason.STOP: 'STOP'>,
#   index=0
# )] create_time=None model_version='gemini-2.5-flash-lite' prompt_feedback=None response_id='tZixaaKjCpjy4-EP0b7cmQQ' usage_metadata=GenerateContentResponseUsageMetadata(
#   candidates_token_count=9,
#   prompt_token_count=9,
#   prompt_tokens_details=[
#     ModalityTokenCount(
#       modality=<MediaModality.TEXT: 'TEXT'>,
#       token_count=9
#     ),
#   ],
#   total_token_count=18
# ) automatic_function_calling_history=[] parsed=None

sdk_http_response=HttpResponse(
  headers=<dict len=11>
) candidates=[Candidate(
  content=Content(
    parts=[
      Part(
        text="""Meow! *stretches out my front paws and gives a long, lazy yawn* 

Purrrrrr... hello there! I'm Neko. Are you here to give me some head scritches, or perhaps a little treat? *rubs my cheek against your hand*""",
        thought_signature=b'\x12\xcd\x05\n\xca\x05\x01\xbe>\xf6\xfbE\xc6\x9d\xfb\xaf/\xe2\xc2\x98y\x9f \xdb\xd8B6\x00\xb1(\x0e\xd80\x17\xb0\xc5>\x14\x06G\xe4\x9c\xfe\xde\xb1j\xf2\xa4\xfd7\r`\xf7\x9641\x8d=\xfa\xc7A\xf9\x86X\xb3\xef\xe8X\td\xdb\x907\x1dy{\xf6\x05n\x10\x84\xaa\x17\xa3x\x10[\xe9AV/=j\x0ed\x92K...'
      ),
    ],
    role='model'
  ),
  finish_reason=<FinishReason.STOP: 'STOP'>,
  index=0
)] create_time=None model_version='gemini-3-flash-preview' prompt_feedback=None response_id='efyyabj9MqCbjuMP1Lvu6A4' usage_metadata=GenerateContentResponseUsageMetadata(
  candidates_token_count=61,
  prompt_token_count=15,
  prompt_tokens_details=[
    ModalityTokenCount(
      modality=<MediaModality.TEXT: 'TEXT'>,
      token_count=15
    ),
  ],
  thoughts_token_count=214,
  total_token_count=290
) automatic_function_calling_history=[] parsed=None