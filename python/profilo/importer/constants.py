"""
Copyright 2018-present, Facebook, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


COUNTER_NAMES = {
    9240581: "THREAD_CPU_TIME",
    9240612: "LOADAVG_1M",
    9240613: "LOADAVG_5M",
    9240614: "LOADAVG_15M",
    9240615: "TOTAL_MEM",
    9240616: "FREE_MEM",
    9240617: "SHARED_MEM",
    9240618: "BUFFER_MEM",
    9240619: "NUM_PROCS",
    9240582: "QL_THREAD_FAULTS_MAJOR",
    9240621: "ALLOC_MMAP_BYTES",
    9240622: "ALLOC_MAX_BYTES",
    9240623: "ALLOC_TOTAL_BYTES",
    9240624: "ALLOC_FREE_BYTES",
    9240579: "PROC_CPU_TIME",
    9240580: "PROC_SW_FAULTS_MAJOR",
    9240593: "GLOBAL_ALLOC_COUNT",
    9240594: "GLOBAL_ALLOC_SIZE",
    9240595: "GLOBAL_GC_INVOCATION_SIZE",
    9240626: "THREAD_WAIT_IN_RUNQUEUE_TIME",
    9240628: "CONTEXT_SWITCHES_VOLUNTARY",
    9240629: "CONTEXT_SWITCHES_INVOLUNTARY",
    9240630: "IOWAIT_COUNT",
    9240631: "IOWAIT_TIME",
    8126501: "AVAILABLE_COUNTERS",
    9240634: "JAVA_FREE_BYTES",
    9240635: "JAVA_MAX_BYTES",
    9240636: "JAVA_ALLOC_BYTES",
    9240637: "JAVA_TOTAL_BYTES",
    9240640: "THREAD_CPU_NUM",
    9240642: "CPU_CORE_FREQUENCY",
    9240643: "MAX_CPU_CORE_FREQUENCY",
    9240604: "PROC_SW_FAULTS_MINOR",
    9240646: "THREAD_SW_FAULTS_MINOR",
    9240645: "PROC_KERNEL_CPU_TIME",
    9240644: "THREAD_KERNEL_CPU_TIME",
    9240647: "VMSTAT_NR_DIRTY",
    9240648: "VMSTAT_NR_WRITEBACK",
    9240649: "VMSTAT_PGPGIN",
    9240650: "VMSTAT_PGPGOUT",
    9240651: "VMSTAT_ALLOCSTALL",
    9240652: "VMSTAT_PAGEOUTRUN",
    9240653: "VMSTAT_KSWAPD_STEAL",
    9240654: "VMSTAT_PGMAJFAULT",
    9240655: "VMSTAT_NR_FREE_PAGES",
    9240664: "GLOBAL_BLOCKING_GC_COUNT",
    9240665: "GLOBAL_GC_TIME",
    9240666: "GLOBAL_BLOCKING_GC_TIME",
    9240656: "PROC_IOWAIT_COUNT",
    9240657: "PROC_IOWAIT_TIME",
    9240658: "PROC_CONTEXT_SWITCHES_INVOLUNTARY",
    9240659: "PROC_CONTEXT_SWITCHES_VOLUNTARY",
}


ANNOTATION_NAMES = {
    8126491: "PROF_ERR_SIG_CRASHES",
    8126492: "PROF_ERR_SLOT_MISSES",
    8126493: "PROF_ERR_STACK_OVERFLOWS",
}