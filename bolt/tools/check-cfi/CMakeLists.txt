set(LLVM_LINK_COMPONENTS
  ${LLVM_TARGETS_TO_BUILD}
  MC
  Object
  Support
  )

if (BOLT_ENABLE_RUNTIME)
  set(BOLT_DRIVER_DEPS "bolt_rt")
else()
  set(BOLT_DRIVER_DEPS "")
endif()

add_bolt_tool(check-cfi
  check-cfi.cpp

  DISABLE_LLVM_LINK_LLVM_DYLIB

  DEPENDS
  ${BOLT_DRIVER_DEPS}
  )

target_link_libraries(check-cfi
  PRIVATE
  LLVMBOLTProfile
  LLVMBOLTRewrite
  LLVMBOLTUtils
  )

add_bolt_tool_symlink(perf2bolt check-cfi)
add_bolt_tool_symlink(llvm-boltdiff check-cfi)

add_dependencies(bolt check-cfi)

include_directories(${BOLT_SOURCE_DIR}/lib)
