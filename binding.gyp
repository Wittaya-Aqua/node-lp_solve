{
    'targets': [
        {
            'target_name': 'lp_solve',
            'dependencies': [
                '<(module_root_dir)/deps/lp_solve/binding.gyp:lp_solve_5.5'
            ],
            'defines': [
            ],
            'include_dirs': [
               "<!(node -e \"require('nan')\")"
            ],
            'sources': [
                'lp_solve.cc',
            ],
            "conditions": [
                [ 'OS!="win"', {
                    "cflags+": [ "-std=c++11" ],
                    "cflags_c+": [ "-std=c++11" ],
                    "cflags_cc+": [ "-std=c++11" ],
                }],
                [ 'OS=="mac"', {
                    "xcode_settings": {
                    "OTHER_CPLUSPLUSFLAGS" : [ "-std=c++11", "-stdlib=libc++" ],
                    "OTHER_LDFLAGS": [ "-stdlib=libc++" ],
                    "MACOSX_DEPLOYMENT_TARGET": "10.7"
                    },
                }],
            ],
        }
    ],
    'configurations': {
        'Release': {
            'msvs_settings': {
                'VCCLCompilerTool': {
                    'ExceptionHandling': 1
                }
            }
        }
    }
}