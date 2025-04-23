from evalscope import TaskConfig, run_task

task_config = TaskConfig(
    api_url='http://0.0.0.0:8000/v1',  # 推理服务地址
    model='DeepSeek-R1-Distill-Qwen-32B',  # 模型名称 (需要与部署时的模型名称一致)
    eval_type='service',  # 评测类型，SERVICE表示评测推理服务
    datasets=['math_500'],  # 数据集名称
    dataset_args={
        'math_500': {
            'few_shot_num': 0,
            # 'prompt_template': '{query}',
            # 'subset_list': ['gpqa_diamond'],
            # 'extra_params': {
            #     'start_date': '2024-08-01',
            #     'end_date': '2024-11-30'
            # },
        },
    },  # 数据集参数
    eval_batch_size=32,  # 发送请求的并发数
    generation_config={
        'max_tokens': 8192,  # 最大生成token数，建议设置为较大值避免输出截断
        'temperature': 0.0,  # 采样温度 (qwen 报告推荐值)
        'top_p': 1.0,  # top-p采样 (qwen 报告推荐值)
        'top_k': -1,  # top-k采样 (qwen 报告推荐值)
        'n': 1,  # 每个请求产生的回复数量
        'request_type': 'chat'
    },
)
run_task(task_config)
