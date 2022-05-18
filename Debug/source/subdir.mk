################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
S_SRCS += \
../source/3140.s 

C_SRCS += \
../source/3140_concur.c \
../source/lock.c \
../source/process.c \
../source/read_csv.c \
../source/run_model.c \
../source/utils.c 

OBJS += \
./source/3140.o \
./source/3140_concur.o \
./source/lock.o \
./source/process.o \
./source/read_csv.o \
./source/run_model.o \
./source/utils.o 

C_DEPS += \
./source/3140_concur.d \
./source/lock.d \
./source/process.d \
./source/read_csv.d \
./source/run_model.d \
./source/utils.d 


# Each subdirectory must supply rules for building sources it contributes
source/%.o: ../source/%.s source/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU Assembler'
	arm-none-eabi-gcc -c -x assembler-with-cpp -D__REDLIB__ -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\board" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\source" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\drivers" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\utilities" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\startup" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\CMSIS" -g3 -mcpu=cortex-m0plus -mthumb -D__REDLIB__ -specs=redlib.specs -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

source/%.o: ../source/%.c source/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MKL46Z256VLL4_cm0plus -DCPU_MKL46Z256VLL4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=1 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=0 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\board" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\source" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\drivers" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\utilities" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\startup" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\CMSIS" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\tflite-micro" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\tflite-micro\third_party\flatbuffers" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\tflite-micro\third_party\ruy" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m0plus -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


