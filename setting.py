// 将设置放入此文件中以覆盖默认设置
{
	"C_Cpp.default.cStandard" : "c11",
	"C_Cpp.errorSquiggles" : "Enabled",
	//C++插件配置
	//C++代码补全时识别上下文，而不是默认fuzz模式
	"C_Cpp.intelliSenseEngine" : "Default",
	"C_Cpp.intelliSenseEngineFallback" : "Disabled",
	"C_Cpp.workspaceParsingPriority" : "low",
	"dtcenter.lintConfig" :
	{
		"checkOnSave" : false,
		"cppcheck.enable" : false,
		"pclint.config" : "/usr1/${env:USERNAME}/dtcenter/demo/flint/config/demo/demo.lnt",
		"pclint.enable" : true,
		"preLintTask" : "code_sync"
	},
	//DTCenter参数配置
	"dtcenter.remoteLinux" :
	{
		"ip" : "10.10.10.x",
		"passwd" : "your-password",
		"user" : "root"
	},
	"editor.minimap.enabled" : false,
	"editor.renderWhitespace" : "all",
	//优先用自定义代码片段进行代码补全
	"editor.snippetSuggestions" : "top",
	"editor.wordWrap" : "wordWrapColumn",
	"editor.wrappingIndent" : "indent",
	"explorer.confirmDelete" : false,
	"extensions.autoUpdate" : false,
	"fileheader.configObj" :
	{
		"autoAdd" : false, // 将该选项设置为true即可开启
		"beforeAnnotation" :
		{
			"py" : "#!/usr/bin/env python\n# -*- coding: utf-8 -*-" // py文件默认，可修改
		}
	},
	"fileheader.cursorMode" : {},
	"fileheader.customMade" :
	{
		"Author" : "Ulysses",
		"Date" : "Do not edit", // 文件创建时间(不变)
		"Description" : "file content",
		"LastEditTime" : "Do not edit" // 文件最后编辑时间
	},
	//解决中文乱码
	"files.autoGuessEncoding" : true,
	"files.autoSave" : "onFocusChange",
	"files.exclude" :
	{
		"**/*.pyc" : true
	},
	"files.trimTrailingWhitespace" : true,
	"files.watcherExclude" :
	{
		"**/*.pyc" : true
	},
	"git.autorefresh" : true,
	"git.hideUntrackedFiles" : true,
	"nextcode.needWarning" : false,
	"python.autoComplete.addBrackets" : true,
	"python.formatting.provider" : "yapf",
	"python.formatting.yapfArgs" : [ "--style", "{based_on_style: chromium, indent_width: 4}" ],
	// 默认对Python文件进行静态检查
	"python.linting.enabled" : true,
	// 默认在Python文件保存时进行静态检查
	"python.linting.lintOnSave" : true,
	// 默认使用pylint对Python文件进行静态检查
	"python.linting.pylintEnabled" : true,
	"telemetry.enableCrashReporter" : false,
	"telemetry.enableTelemetry" : false,
	"terminal.integrated.rendererType" : "dom",
	//控制终端保持在缓冲区的最大行数
	"terminal.integrated.scrollback" : 10000,
	"window.menuBarVisibility" : "default",
	"window.zoomLevel" : 0,
	"workbench.colorCustomizations" :
	{
		"editorCursor.foreground" : "#e9e6e6",
		"terminalCursor.foreground" : "#ffff00"
	},

	"code-runner.executorMap": {
		"javascript": "node",
		//"php": "C:\\php\\php.exe",
		"python": "set PYTHONIOENCODING=utf8 && python3",
		"perl": "perl",
		"ruby": "C:\\Ruby23-x64\\bin\\ruby.exe",
		"go": "go run",
		"html": "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"",
		"java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
		"c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt"
	},
	"code-runner.respectShebang": false,
	"python.jediEnabled": false,
}
