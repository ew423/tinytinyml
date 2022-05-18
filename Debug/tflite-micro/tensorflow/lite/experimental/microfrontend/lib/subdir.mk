################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/fft_io.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/filterbank.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/filterbank_io.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/filterbank_util.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_io.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_main.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_memmap_generator.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_memmap_main.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_util.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_lut.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_scale.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_scale_io.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_scale_util.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/noise_reduction.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/noise_reduction_io.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/noise_reduction_util.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control_util.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/window.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/window_io.c \
../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/window_util.c 

OBJS += \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/fft_io.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/filterbank.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/filterbank_io.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/filterbank_util.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_io.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_main.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_memmap_generator.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_memmap_main.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_util.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_lut.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_scale.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_scale_io.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_scale_util.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/noise_reduction.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/noise_reduction_io.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/noise_reduction_util.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control_util.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/window.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/window_io.o \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/window_util.o 

C_DEPS += \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/fft_io.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/filterbank.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/filterbank_io.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/filterbank_util.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_io.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_main.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_memmap_generator.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_memmap_main.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/frontend_util.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_lut.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_scale.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_scale_io.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/log_scale_util.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/noise_reduction.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/noise_reduction_io.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/noise_reduction_util.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control_util.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/window.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/window_io.d \
./tflite-micro/tensorflow/lite/experimental/microfrontend/lib/window_util.d 


# Each subdirectory must supply rules for building sources it contributes
tflite-micro/tensorflow/lite/experimental/microfrontend/lib/%.o: ../tflite-micro/tensorflow/lite/experimental/microfrontend/lib/%.c tflite-micro/tensorflow/lite/experimental/microfrontend/lib/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MKL46Z256VLL4_cm0plus -DCPU_MKL46Z256VLL4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=1 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=0 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\board" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\source" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\drivers" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\utilities" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\startup" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\CMSIS" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\tflite-micro" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\tflite-micro\third_party\flatbuffers" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\tflite-micro\third_party\ruy" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m0plus -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


