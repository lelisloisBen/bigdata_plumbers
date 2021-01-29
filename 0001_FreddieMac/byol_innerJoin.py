from pyspark.sql import functions as F
from pyspark import SparkFiles
from pyspark.sql import SparkSession



spark = SparkSession.builder.appName('byolInnerJoinTest2').getOrCreate()

s3_out_uri="s3://freddie-mac-sandbox-raw-plus/byol/parquet/"

df_laus=spark.read.parquet("s3://freddie-mac-sandbox-raw-plus/rimes/index/caci_idx_std/parquet/")
df_laus.createOrReplaceTempView("input_laus")
df_borr=spark.read.parquet("s3://freddie-mac-sandbox-raw-plus/rimes/index/ftse_idx_std/parquet/")
df_borr.createOrReplaceTempView("input_borr")

df_joined=spark.sql("""SELECT
                       a.accruedInterest,
                       a.adjustedDuration,
                       a.asiaPacificFlag,
                       a.assetSwap,
                       a.assetSwapDailyChange,
                       a.averageBidSpread,
                       a.averageCoupon,
                       a.averageLife,
                       a.averageModifiedDuration,
                       a.averageOAS,
                       a.averageOptionAdjustedDuration,
                       a.averageRating,
                       a.averageSpread,
                       a.averageTerm,
                       a.averageYield,
                       a.averageZeroVolatilitySpread,
                       a.currencyBase,
                       a.cashValue,
                       a.divisorEOD,
                       a.commonFrequencyModifiedDuration,
                       a.convexity,
                       a.convexityToWorst,
                       a.couponReturnDailyBase,
                       a.ID_index,
                       a.currencyReturnMTDBase,
                       a.returnDailyBase,
                       a.date,
                       a.indexDescription,
                       a.developedEmergingFlag,
                       a.dividendYield,
                       a.durationToWorst,
                       a.effectiveConvexity,
                       a.effectiveDuration,
                       a.effectiveInterestRateDuration,
                       a.effectiveYield,
                       a.excessReturnBase,
                       a.excessReturnDailyBase,
                       a.excessSwapReturnDailyBase,
                       a.growthFlag,
                       a.hedgeFlag,
                       a.hedgedRatio,
                       a.hedgedCurrency,
                       a.inceptionReturnBase,
                       a.incomeReturnBase,
                       a.indexValueBase,
                       a.interestIndexValue,
                       a.interestReturnBase,
                       a.islamicFlag,
                       a.largeCapFlag,
                       a.macaulayDuration,
                       a.marketValueBase,
                       a.marketWeightedCoupon,
                       a.maturityDate,
                       a.maturityToWAL,
                       a.microCapFlag,
                       a.midCapFlag,
                       a.modifiedDuration,
                       a.modifiedDurationToWorst,
                       a.constituentCount,
                       a.constituentCountReturnUniverse,
                       a.notionalValueOutstanding,
                       a.notionalValueOutstandingCAD,
                       a.issuerCount,
                       a.numericRating,
                       a.oas,
                       a.oasDailyChange,
                       a.oasLIBOR,
                       a.parAmount,
                       a.parWeightedCoupon,
                       a.paydownConditionalPrepaymentRate,
                       a.paydownReturnMTDBase,
                       a.principalReturnDailyBase,
                       a.quality,
                       a.returnType,
                       a.rimesSourceCode,
                       a.rimesSourceDescription,
                       a.ID_rimesSymbol,
                       a.sector,
                       a.sectorWeight,
                       a.session,
                       a.smallCapFlag,
                       a.spreadDuration,
                       a.spreadDurationPercentChangeDaily,
                       a.spreadOverTreasury,
                       a.spreadToMaturity,
                       a.spreadToWorst,
                       a.spreadToWorstPercentChangeDaily,
                       a.strippedSovereignDuration,
                       a.strippedSpread,
                       a.strippedSpreadDuration,
                       a.strippedTreasuryDuration,
                       a.strippedYield,
                       a.strippedYieldToMaturity,
                       a.term,
                       a.termWeight,
                       a.valueFlag,
                       a.ID_vendorIndex,
                       a.weightedAverageCoupon,
                       a.weightedAverageLife,
                       a.weightedAverageMaturity,
                       a.yield,
                       a.yieldToMaturity,
                       a.yieldToWorst,
                       a.yearsToWorst,
                       a.bidValue,
                       a.feedVersion,
                       a.ID_mdsIndex,
                       a.staleFeedFlag
                       FROM input_laus a JOIN input_borr b
                       ON a.currencyBase = b.currencyBase""")


df_inner_joined_final=df_joined.withColumn('edptimestamp', F.current_timestamp())

a=df_inner_joined_final.count()

print(f'Staging count is :{a}')

df_inner_joined_final.write.format("parquet").mode("overwrite").save(s3_out_uri)

df_read_s3=spark.read.parquet(s3_out_uri)

b=df_read_s3.count()

print(f'Final count is :{b}')