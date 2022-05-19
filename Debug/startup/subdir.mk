################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../startup/startup_mkl46z4.c 

OBJS += \
./startup/startup_mkl46z4.o 

C_DEPS += \
./startup/startup_mkl46z4.d 


# Each subdirectory must supply rules for building sources it contributes
startup/%.o: ../startup/%.c startup/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MKL46Z256VLL4_cm0plus -DCPU_MKL46Z256VLL4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=1 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=0 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\board" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\source" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\drivers" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\utilities" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\startup" -I"C:\Users\evely\Documents\MCUXpressoIDE_11.5.0_7232\workspace\CS3420_Tiny_TinyML\CMSIS" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m0plus -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


