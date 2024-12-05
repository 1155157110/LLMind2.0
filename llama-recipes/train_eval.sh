CUDA_VISIBLE_DEVICES=0,1
TORCH_DISTRIBUTED_DEBUG=DETAIL

DIR=your_output_dir
LOG_PATH=logs/$DIR
BATCH_SIZE=2
TRAIN_EPOCHS=2

[ -d $LOG_PATH ] || mkdir -p $LOG_PATH

torchrun > $LOG_PATH/epoch1.txt \
    --nnodes 1 --nproc_per_node 2 recipes/finetuning/finetuning.py \
    --enable_fsdp --low_cpu_fsdp --use_peft --peft_method lora \
    --model_name ../llama-2-7b \
    --fsdp_config.pure_bf16 \
    --batch_size_training $BATCH_SIZE \
    --dataset custom_dataset \
    --custom_dataset.file "process_dataset.py:get_preprocessed_custom" \
    --output_dir ../finetune_results/$DIR/epoch$TRAIN_EPOCHS \
    --num_epochs $TRAIN_EPOCHS \
    --save_model
